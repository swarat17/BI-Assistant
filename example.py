from newsapi import NewsApiClient
import json

# Init
newsapi = NewsApiClient(api_key="7625cb5e7efb44b98bea3d6c8a4100c2")

# Example: Fetch OpenAI news
articles = newsapi.get_everything(
    q='OpenAI OR ChatGPT OR GPT-4',
    from_param='2025-08-01',
    to='2025-08-31',
    language='en',
    sort_by='publishedAt',
    page_size=10
)

# Normalize
normalized = []
for a in articles['articles']:
    normalized.append({
        "source": "news",
        "company": "OpenAI",
        "title": a['title'],
        "date": a['publishedAt'],
        "url": a['url'],
        "content": a['description'] or a['content']
    })

# Save
with open("news_openai.json", "w", encoding="utf-8") as f:
    json.dump(normalized, f, indent=2)

print("Saved", len(normalized), "articles.")