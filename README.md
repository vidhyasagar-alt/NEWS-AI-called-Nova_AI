🎤 Nova AI – Voice Controlled News Assistant










🚀 A smart voice-powered AI assistant that listens, understands, and delivers real-time news — completely hands-free.

✨ Overview

Nova AI is a modern voice assistant built with Python that uses speech recognition + AI + APIs to provide real-time news updates.

Just say “Hello Nova”, ask your query, and Nova responds instantly 🎙️

🚀 Features
🎙️ Wake word detection (“Hello Nova”)
🧠 AI-powered speech recognition (Whisper)
📰 Real-time news fetching
🔊 Voice responses (Text-to-Speech)
⚡ Hands-free interaction
🧩 Modular & scalable architecture
🧠 How It Works
🎤 Voice Input → 🧠 Whisper → 🔍 Query → 📰 News API → 🔊 Voice Output
🛠️ Tech Stack
Python
Whisper (Speech Recognition)
FFmpeg (Audio Processing)
SoundDevice
News API
Text-to-Speech (TTS)
📂 Project Structure
nova-news-ai/
│
├── core/
│   ├── wake_word.py
│   ├── speech_input.py
│   ├── speech_output.py
│   ├── news_fetcher.py
│
├── nova.py
├── config.py
└── README.md
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/vidhyasagar-alt
cd nova-news-ai
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Install FFmpeg

Download from:
👉 https://www.gyan.dev/ffmpeg/builds/

Then add to PATH or use:

import os
os.environ["PATH"] += os.pathsep + r"C:\path\to\ffmpeg\bin"
4️⃣ Add API Key

Edit config.py:

NEWS_API_KEY = "your_api_key_here"
▶️ Usage
python nova.py
🎯 Demo Interaction
User: Hello Nova
Nova: Hello Sir, what news do you want?

User: Sports news
Nova: Here are the latest sports headlines...
🔥 Why This Project Stands Out
💡 Real-world AI use case
🎙️ Fully voice-controlled system
⚡ Clean modular architecture
🚀 Beginner-friendly yet powerful
🧠 Uses modern AI (Whisper)
🚀 Future Improvements
🎧 Real-time continuous listening
🤖 ChatGPT conversational mode
🌐 Multi-language support
🖥️ GUI Dashboard
⚡ Faster streaming responses
👨‍💻 Author

Vidhya Sagar

🔗 GitHub: https://github.com/vidhyasagar-alt
🔗 LinkedIn: https://www.linkedin.com/in/vidhya-sagar-4bba5339b
⭐ Show Your Support

If you like this project:

👉 Give it a ⭐ on GitHub
👉 Share it with others
👉 Fork and improve it

📜 License

MIT License © 2026
