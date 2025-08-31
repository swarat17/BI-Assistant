from eventregistry import EventRegistry, QueryArticlesIter
import json

# Create client (sign up at newsapi.ai for a free API key)
er = EventRegistry(apiKey="4e211009-aea6-4991-ad67-b00ef01a4f51", allowUseOfArchive=True)

# Define competitors
companies = [
    "OpenAI"
    # ,"Anthropic", "Cohere", "Hugging Face", "Stability AI"
]

all_articles = []

for name in companies:
    query = QueryArticlesIter(
        keywords = name,
        # Optionally add filters like date range, language etc.
    )
    # Fetch up to 50 articles per company
    for art in query.execQuery(er, maxItems=50):
        all_articles.append({
            "source": art.get("source", {}).get("title", ""),
            "company": name,
            "title": art.get("title"),
            "date": art.get("dateTime"),
            "url": art.get("url"),
            "content": art.get("body"),  # full article
        })

print(f"Fetched {len(all_articles)} articles.")

# Save to JSON for downstream pipeline
with open("genai_competitors_articles.json", "w", encoding="utf-8") as f:
    json.dump(all_articles, f, indent=2)