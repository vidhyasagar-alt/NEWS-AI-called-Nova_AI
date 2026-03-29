import os

# 🔧 FIX: Ensure FFmpeg is available for Whisper
os.environ["PATH"] += os.pathsep + r"C:\Users\ELCOT\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin"

import time
from core.wake_word import wait_for_wake_word
from core.speech_input import listen_for_command
from core.speech_output import speak
from core.news_fetcher import fetch_news


def run_nova():
    print("=" * 60)
    print("        NOVA - Your AI News Assistant        ")
    print("=" * 60)
    print("Nova is starting up... Please wait.\n")

    speak("Hello! I am Nova, your personal AI news assistant. Say Hello Nova to wake me up.")
    print("[Nova is ready] Say 'Hello Nova' to activate.\n")

    while True:
        try:
            # Step 1: Wait for wake word "Hello Nova"
            wake_detected = wait_for_wake_word()

            if wake_detected:
                speak("Hello Sir, what news do you want?")
                print("\n[Nova] Hello Sir, what news do you want?\n")

                # Step 2: Listen for the user's news query
                print("[Listening for your query...]\n")
                user_query = listen_for_command()

                if not user_query:
                    speak("Sorry, I did not catch that. Please try again.")
                    print("[Nova] Sorry, I did not catch that.\n")
                    continue

                print(f"[You said] {user_query}\n")

                # Step 3: Fetch news based on query
                print("[Nova is fetching news...]\n")
                speak(f"Searching for news about {user_query}. Please wait.")

                news_text, news_articles = fetch_news(user_query)

                if not news_articles:
                    speak("Sorry, I could not find any news on that topic right now.")
                    print("[Nova] No news found.\n")
                    continue

                # Step 4: Display and speak the news
                print("=" * 60)
                print(f"  TOP NEWS: {user_query.upper()}")
                print("=" * 60)

                for i, article in enumerate(news_articles, 1):
                    title = article.get("title", "No title")
                    source = article.get("source", {}).get("name", "Unknown source")
                    description = article.get("description") or "No description available."
                    url = article.get("url", "")

                    print(f"\n[{i}] {title}")
                    print(f"    Source  : {source}")
                    print(f"    Summary : {description}")
                    print(f"    Link    : {url}")
                    print("-" * 60)

                # Speak the news summary
                speak(news_text)

                print("\n[Nova] Say 'Hello Nova' again for more news.\n")

        except KeyboardInterrupt:
            print("\n[Nova] Shutting down. Goodbye!")
            speak("Goodbye Sir. Have a great day!")
            break
        except Exception as e:
            print(f"[Error] {e}")
            time.sleep(2)


if __name__ == "__main__":
    run_nova()