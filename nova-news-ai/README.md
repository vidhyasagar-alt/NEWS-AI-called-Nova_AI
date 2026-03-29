# 🌍 NOVA - AI News Assistant

Nova is your personal AI-powered news assistant.
Say **"Hello Nova"** and ask for any news — sports, crime, politics, world news — from any country or region.
Nova reads the news out loud AND displays it as text in the terminal.

---

## 📁 Project Structure

```
nova-news-ai/
├── main.py                   ← Run this file
├── core/
│   ├── wake_word.py          ← Detects "Hello Nova"
│   ├── speech_input.py       ← Mic → Text (Whisper)
│   ├── speech_output.py      ← Text → Audio (gTTS)
│   └── news_fetcher.py       ← Fetches news from NewsAPI
├── config/
│   └── settings.py           ← All settings
├── logs/
├── assets/
├── requirements.txt
└── .env                      ← Your API key goes here
```

---

## ⚙️ SETUP (Windows)

### Step 1 — Install Python
Make sure Python 3.9+ is installed:
https://www.python.org/downloads/

### Step 2 — Install FFmpeg (Required for Whisper)
1. Download from: https://ffmpeg.org/download.html
2. Extract and add the `bin` folder to your Windows PATH
3. Verify: open CMD and type `ffmpeg -version`

### Step 3 — Install PyAudio (Windows specific)
```bash
pip install pipwin
pipwin install pyaudio
```

### Step 4 — Install all dependencies
```bash
pip install -r requirements.txt
```

### Step 5 — Get your FREE NewsAPI Key
1. Go to: https://newsapi.org/register
2. Sign up for free
3. Copy your API key

### Step 6 — Add your API Key
Open the `.env` file and replace:
```
NEWS_API_KEY=YOUR_NEWSAPI_KEY_HERE
```
with your actual key:
```
NEWS_API_KEY=abc123yourkeyhere
```

---

## ▶️ HOW TO RUN

Open terminal in VS Code and run:
```bash
python main.py
```

---

## 🗣️ HOW TO USE

1. Nova starts and says: *"Say Hello Nova to wake me up"*
2. Say: **"Hello Nova"**
3. Nova replies: *"Hello Sir, what news do you want?"*
4. Say your query, examples:
   - *"Sports news"*
   - *"Cricket latest"*
   - *"Politics in USA"*
   - *"Crime news India"*
   - *"Technology news"*
   - *"World news today"*
5. Nova **displays** the news as text AND **reads it aloud**

---

## 🛑 To Stop Nova
Press `Ctrl + C` in the terminal.
