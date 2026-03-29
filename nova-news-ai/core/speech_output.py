from gtts import gTTS
import pygame
import tempfile
import os
import time

# Initialize pygame mixer for audio playback
pygame.mixer.init()

def speak(text):
    """
    Converts text to speech using gTTS and plays it immediately.
    Also prints the text to the terminal.
    """
    if not text or not text.strip():
        return

    print(f"[Nova Speaking] {text}\n")

    try:
        # Generate speech audio
        tts = gTTS(text=text, lang='en', slow=False)

        # Save to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
            tmp_path = tmp_file.name
            tts.save(tmp_path)

        # Play the audio
        pygame.mixer.music.load(tmp_path)
        pygame.mixer.music.play()

        # Wait until audio finishes
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        # Cleanup
        pygame.mixer.music.unload()
        os.remove(tmp_path)

    except Exception as e:
        print(f"[TTS Error] {e}")
        print(f"[Text Fallback] {text}")
