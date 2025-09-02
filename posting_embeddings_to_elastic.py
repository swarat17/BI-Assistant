from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
import json

# -----------------------
# CONFIG
# -----------------------
JSON_FILE = "genai_competitors_articles_translated.json"
ES_INDEX = "bi-assistant-1729"

# Replace this with your actual Elasticsearch URL
ES_URL = "https://my-elasticsearch-project-bff9ea.es.us-central1.gcp.elastic.cloud:443"

# # If your ES cluster requires authentication:
# # Option 1: Basic Auth (username/password)
# es = Elasticsearch(
#     ES_URL,
#     basic_auth=("elastic", "your_password_here")
# )

# Option 2: API Key Auth (if preferred, comment above and use this)
es = Elasticsearch(
    ES_URL,
    api_key="ZVZyWEM1a0JMSUdVOUlUSnJrUU06SnhxN19DR0Q0RUZGbGUxZ25NdEFEdw=="
)

# -----------------------
# Load Sentence-BERT model
# -----------------------
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")  
# → 384-d embeddings

# -----------------------
# Create index mapping (if not already exists)
# -----------------------
if not es.indices.exists(index=ES_INDEX):
    es.indices.create(
        index=ES_INDEX,
        body={
            "mappings": {
                "properties": {
                    "source": {"type": "keyword"},
                    "company": {"type": "keyword"},
                    "title": {"type": "text"},
                    "date": {"type": "date"},
                    "url": {"type": "keyword"},
                    "content": {"type": "text"},
                    "embedding": {
                        "type": "dense_vector",
                        "dims": 384
                    }
                }
            }
        }
    )

# -----------------------
# Load JSON articles
# -----------------------
with open(JSON_FILE, "r", encoding="utf-8") as f:
    articles = json.load(f)

# -----------------------
# Generate embeddings & index docs
# -----------------------
for i, article in enumerate(articles):
    content = article.get("content", "")
    if not content.strip():
        continue
    
    # Generate embedding
    embedding = model.encode(content).tolist()

    # Prepare doc
    doc = {
        "source": article.get("source"),
        "company": article.get("company"),
        "title": article.get("title"),
        "date": article.get("date"),
        "url": article.get("url"),
        "content": content,
        "embedding": embedding
    }

    # Index into Elasticsearch
    es.index(index=ES_INDEX, id=i, body=doc)

print(f"✅ Articles embedded with Sentence-BERT and stored in Elasticsearch index: {ES_INDEX}")
