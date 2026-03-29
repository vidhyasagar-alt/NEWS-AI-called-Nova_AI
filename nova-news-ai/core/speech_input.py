import whisper
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile as wav
import os

print("[Whisper] Loading speech model... (first time may take a moment)")
model = whisper.load_model("base")
print("[Whisper] Model loaded.\n")


def calibrate_noise(sample_rate=16000, calibration_seconds=1.5):
    """
    Listens to room noise for 1.5 seconds and returns a dynamic threshold.
    Sets threshold 2.2x above background so fan/AC noise never triggers detection.
    """
    print("[Calibrating] Measuring background noise... stay quiet for 1.5 seconds.")
    audio = sd.rec(
        int(calibration_seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype='int16'
    )
    sd.wait()
    rms = np.sqrt(np.mean(audio.astype(np.float32) ** 2))
    threshold = max(rms * 2.2, 300)
    print(f"[Calibrated] Background RMS: {rms:.1f} | Voice threshold: {threshold:.1f}\n")
    return threshold


# Calibrate once at startup — adapts to your room automatically
NOISE_THRESHOLD = calibrate_noise()


def record_until_silence(
    sample_rate=16000,
    silence_timeout=2.0,
    min_speech_seconds=0.8,
    max_duration=15,
    chunk_duration=0.3
):
    """
    Records in small chunks, stops automatically when you stop speaking.
    Uses dynamic threshold so fan/AC noise is ignored.
    """
    chunk_size     = int(sample_rate * chunk_duration)
    audio_chunks   = []
    silence_chunks = 0
    speech_chunks  = 0
    silence_limit  = int(silence_timeout    / chunk_duration)
    max_chunks     = int(max_duration       / chunk_duration)
    min_speech_chk = int(min_speech_seconds / chunk_duration)

    print("[Listening] Speak now — Nova stops when you go silent...")

    with sd.InputStream(samplerate=sample_rate, channels=1, dtype='int16') as stream:
        for _ in range(max_chunks):
            chunk, _ = stream.read(chunk_size)
            audio_chunks.append(chunk.copy())

            rms = np.sqrt(np.mean(chunk.astype(np.float32) ** 2))

            if rms > NOISE_THRESHOLD:
                speech_chunks += 1
                silence_chunks = 0
            else:
                silence_chunks += 1

            if speech_chunks >= min_speech_chk and silence_chunks >= silence_limit:
                print("[Recording done] Silence detected — transcribing...\n")
                break

    audio_data = np.concatenate(audio_chunks, axis=0)
    return audio_data, sample_rate


def listen_for_command():
    """
    Records until silence, transcribes with Whisper, returns text or None.
    """
    audio_data, sample_rate = record_until_silence()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
        tmp_path = tmp_file.name
        wav.write(tmp_path, sample_rate, audio_data)

    try:
        result = model.transcribe(tmp_path, language="en")
        text = result["text"]
        if isinstance(text, list):
            text = text[0] if text else ""
        text = text.strip()
        print(f"[Transcribed] {text}")
        return text if text else None
    except Exception as e:
        print(f"[Whisper Error] {e}")
        return None
    finally:
        os.remove(tmp_path)