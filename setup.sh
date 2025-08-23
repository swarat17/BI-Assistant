#!/bin/bash


# Top-level files
touch requirements.txt docker-compose.yml

# .github workflows
mkdir -p .github/workflows
touch .github/workflows/ci-cd.yml

# Backend
mkdir -p backend/{routers,services,models}
touch backend/main.py
touch backend/config.py
touch backend/routers/{ask.py,feedback.py,health.py}
touch backend/services/{rag_pipeline.py,embeddings.py,feedback_rl.py}
touch backend/models/{request_models.py,feedback_models.py}

# Workflows
mkdir -p workflows
touch workflows/{n8n_news_workflow.json,n8n_github_workflow.json,n8n_filings_workflow.json,langgraph_pipeline.py}

# Reinforcement Learning
mkdir -p rl
touch rl/{bandit.py,ppo_experiment.py,feedback_store.json}

# Frontend
mkdir -p frontend/static
touch frontend/streamlit_app.py

# Docs
mkdir -p docs
touch docs/{architecture.png,api_flow.png,workflows.png,demo.gif}

echo "✅ Project structure created successfully!"