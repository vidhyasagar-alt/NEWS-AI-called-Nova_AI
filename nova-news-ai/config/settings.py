import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- API Keys ---
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "49b00fe3e9a04879838f7643ab73b9a3")

# --- Speech Settings ---
TTS_LANGUAGE = "en"          # Language for gTTS
WHISPER_MODEL = "base"       # Whisper model: tiny, base, small, medium, large
RECORD_DURATION = 6          # Seconds to record user command
SAMPLE_RATE = 16000          # Audio sample rate for Whisper

# --- Wake Word ---
WAKE_WORD = "hello nova"     # Trigger phrase (lowercase)

# --- News Settings ---
MAX_ARTICLES = 5             # Number of news articles to fetch per query
NEWS_LANGUAGE = "en"         # Language filter for NewsAPI
NEWS_SORT_BY = "publishedAt" # Options: relevancy, popularity, publishedAt
