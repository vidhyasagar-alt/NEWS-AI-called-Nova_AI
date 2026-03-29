import requests
from config.settings import NEWS_API_KEY

# Category keywords mapping for smarter fetching
CATEGORY_MAP = {
    "sports": "sports",
    "cricket": "cricket",
    "football": "football",
    "soccer": "soccer",
    "basketball": "basketball",
    "crime": "crime",
    "politics": "politics",
    "technology": "technology",
    "tech": "technology",
    "business": "business",
    "health": "health",
    "science": "science",
    "entertainment": "entertainment",
    "weather": "weather",
    "india": "india",
    "usa": "united states",
    "uk": "united kingdom",
    "world": "world news",
}

def detect_category(query):
    """Maps user query to a NewsAPI-friendly search term."""
    q_lower = query.lower()
    for keyword, mapped in CATEGORY_MAP.items():
        if keyword in q_lower:
            return mapped
    return query  # Use raw query if no mapping found

def fetch_news(query, max_articles=5):
    """
    Fetches top news articles from NewsAPI based on user query.
    Returns:
        - news_text (str): A readable spoken summary of all headlines
        - articles (list): Full article objects for display
    """
    if not NEWS_API_KEY or NEWS_API_KEY == "YOUR_NEWSAPI_KEY_HERE":
        return "Please add your NewsAPI key in the .env file.", []

    search_term = detect_category(query)

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": search_term,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": max_articles,
        "apiKey": NEWS_API_KEY,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data.get("status") != "ok":
            return "Sorry, I could not retrieve news at this time.", []

        articles = data.get("articles", [])

        if not articles:
            return f"No recent news found for {query}.", []

        # Build spoken summary
        lines = [f"Here are the top {len(articles)} news headlines about {query}."]
        for i, article in enumerate(articles, 1):
            title = article.get("title", "").split(" - ")[0]  # Remove source suffix
            source = article.get("source", {}).get("name", "")
            desc = article.get("description") or ""

            # Spoken line per article
            lines.append(f"News {i}. {title}. Reported by {source}.")
            if desc:
                # Trim description to keep speech concise
                short_desc = desc[:180] + "..." if len(desc) > 180 else desc
                lines.append(short_desc)

        news_text = " ".join(lines)
        return news_text, articles

    except requests.exceptions.ConnectionError:
        return "No internet connection. Please check your network.", []
    except Exception as e:
        return f"An error occurred while fetching news: {str(e)}", []
