🎙️ Nova AI — Voice-Controlled News Assistant

Say it. Hear it. Know it. Nova AI delivers real-time news through a fully hands-free, voice-controlled interface powered by OpenAI Whisper.

Show Image
Show Image
Show Image
Show Image

🧠 What Is Nova AI?
Nova AI is an end-to-end voice assistant pipeline that listens for a wake word, transcribes natural speech using OpenAI Whisper, fetches live news via NewsAPI, and responds aloud using Text-to-Speech — all without touching a keyboard.
This project demonstrates a complete integration of speech AI, real-time APIs, and modular software design — built entirely in Python.

✨ Key Features
FeatureDescription🎙️ Wake Word DetectionActivates on "Hello Nova" — always listening, never intrusive🧠 Whisper ASROn-device speech-to-text using OpenAI's Whisper model📰 Live News FetchingReal-time headlines via NewsAPI (sports, tech, world & more)🔊 Voice ResponsesNatural text-to-speech output for a hands-free experience⚡ Zero UI RequiredFully operable without a screen or keyboard🧩 Modular ArchitectureClean separation of concerns — easy to extend or swap components

🏗️ System Architecture
🎤 Microphone Input
      ↓
🔍 Wake Word Detector  ("Hello Nova")
      ↓
🧠 Whisper ASR         (Speech → Text)
      ↓
📰 NewsAPI Fetcher      (Query → Headlines)
      ↓
🔊 TTS Engine           (Text → Speech Output)

📂 Project Structure
nova-news-ai/
│
├── core/
│   ├── wake_word.py       # Wake word detection loop
│   ├── speech_input.py    # Microphone capture + Whisper transcription
│   ├── speech_output.py   # Text-to-Speech engine
│   └── news_fetcher.py    # NewsAPI integration & query parsing
│
├── nova.py                # Main entry point & orchestration
├── config.py              # API keys & configuration
└── requirements.txt

🛠️ Tech Stack

Python 3.10+ — Core language
OpenAI Whisper — State-of-the-art on-device speech recognition
SoundDevice — Low-latency microphone audio capture
FFmpeg — Audio format processing
NewsAPI — Real-time global news headlines
pyttsx3 / gTTS — Text-to-Speech voice output


⚙️ Getting Started
1. Clone the repository
bashgit clone https://github.com/vidhyasagar-alt/nova-news-ai
cd nova-news-ai
2. Install Python dependencies
bashpip install -r requirements.txt
3. Install FFmpeg
Download from gyan.dev/ffmpeg/builds and add to your system PATH, or configure it in code:
pythonimport os
os.environ["PATH"] += os.pathsep + r"C:\path\to\ffmpeg\bin"
4. Configure your API key
Edit config.py:
pythonNEWS_API_KEY = "your_newsapi_key_here"
Get a free key at newsapi.org.
5. Run Nova
bashpython nova.py
```

---

## 🎯 Demo Interaction
```
> python nova.py

[Nova is listening...]

User  → "Hello Nova"
Nova  → "Hello! What news would you like today?"

User  → "Give me the latest tech news"
Nova  → "Here are today's top tech headlines:
          1. OpenAI announces new model series...
          2. Google DeepMind releases AlphaFold 3...
          ..."

💡 Why This Project?
Most news apps are passive — you scroll, you click, you read. Nova AI is active — it listens, understands intent, and responds. This reflects how AI assistants will work in the real world: voice-native, always on, and context-aware.
This project was built to explore the full pipeline from raw audio to intelligent output, with practical applications in:

Accessibility tools for hands-free users
Smart home / IoT integrations
In-vehicle or wearable assistant systems
Voice-first interfaces for any domain


🚀 Roadmap

 Continuous background listening (no push-to-talk)
 GPT-powered conversational follow-ups
 Multi-language support (Hindi, Tamil, Spanish, etc.)
 GUI dashboard with live transcript display
 Streaming responses for lower latency
 Docker containerization for easy deployment


👨‍💻 Author
Vidhya Sagar
Passionate about building AI systems that interact naturally with humans.
🔗 GitHub · LinkedIn

📜 License
MIT License © 2026 Vidhya Sagar — free to use, modify, and distribute.

If Nova AI impressed you, consider giving it a ⭐ — it helps others discover the project.
