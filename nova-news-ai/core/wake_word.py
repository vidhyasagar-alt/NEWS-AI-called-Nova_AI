import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile as wav
import os
from faster_whisper import WhisperModel

print("[Wake Word] Loading Whisper for wake word detection...")
wake_model = WhisperModel("small", device="cpu", compute_type="int8")
print("[Wake Word] Ready.\n")

WAKE_VARIATIONS = [
    "hello nova", "hey nova", "hi nova",
    "nova", "helo nova", "hallow nova",
    "hela nova",
]


def calibrate_noise(sample_rate=16000, calibration_seconds=1.5):
    """
    Measures background noise and returns a dynamic threshold.
    Runs once at startup — handles fan, AC, and room noise automatically.
    """
    print("[Wake Word Calibrating] Stay quiet for 1.5 seconds...")
    audio = sd.rec(
        int(calibration_seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype='int16'
    )
    sd.wait()
    rms = np.sqrt(np.mean(audio.astype(np.float32) ** 2))
    threshold = max(rms * 2.2, 300)
    print(f"[Wake Word Calibrated] Background RMS: {rms:.1f} | Threshold: {threshold:.1f}\n")
    return threshold


# Calibrate once at startup
NOISE_THRESHOLD = calibrate_noise()


def record_wake_chunk(
    sample_rate=16000,
    silence_timeout=1.2,
    max_duration=5,
    chunk_duration=0.2
):
    """
    Records a short clip stopping as soon as silence is detected after speech.
    Ignores constant fan/AC noise using the calibrated threshold.
    """
    chunk_size      = int(sample_rate * chunk_duration)
    audio_chunks    = []
    silence_chunks  = 0
    speech_detected = False
    silence_limit   = int(silence_timeout / chunk_duration)
    max_chunks      = int(max_duration    / chunk_duration)

    with sd.InputStream(samplerate=sample_rate, channels=1, dtype='int16') as stream:
        for _ in range(max_chunks):
            chunk, _ = stream.read(chunk_size)
            audio_chunks.append(chunk.copy())

            rms = np.sqrt(np.mean(chunk.astype(np.float32) ** 2))

            if rms > NOISE_THRESHOLD:
                speech_detected = True
                silence_chunks  = 0
            else:
                if speech_detected:
                    silence_chunks += 1

            if speech_detected and silence_chunks >= silence_limit:
                break

    audio_data = np.concatenate(audio_chunks, axis=0)
    return audio_data, sample_rate, speech_detected


def wait_for_wake_word(wake_word="hello nova"):
    """
    Listens in a loop and returns True as soon as wake word is detected.
    Skips Whisper entirely when no voice energy is detected — stays fast.
    """
    print("[Wake Word Listener] Listening for 'Hello Nova'... (speak clearly)")

    while True:
        try:
            audio_data, sample_rate, speech_detected = record_wake_chunk()

            # Skip transcription if only background noise detected
            if not speech_detected:
                continue

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
                tmp_path = tmp_file.name
                wav.write(tmp_path, sample_rate, audio_data)

            segments, _ = wake_model.transcribe(tmp_path, language="en")
            text = " ".join([seg.text for seg in segments]).strip().lower()

            os.remove(tmp_path)

            if text:
                print(f"[Heard] {text}")

            for variation in WAKE_VARIATIONS:
                if variation in text:
                    print("[Wake Word Detected!] Activating Nova...\n")
                    return True

        except Exception as e:
            print(f"[Wake Word Error] {e}")
            continue