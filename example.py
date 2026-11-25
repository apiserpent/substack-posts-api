"""Substack Posts API - Python example.

Docs: https://apiserpent.com/substack-api
Run:  SERPENT_API_KEY=sk_live_... python example.py
"""
import os
import sys

import requests

API_KEY = os.environ.get("SERPENT_API_KEY")
if not API_KEY:
    sys.exit("Set the SERPENT_API_KEY environment variable first.")

params = {"publication": "astralcodexten", "sort": "top"}

response = requests.get(
    "https://apiserpent.com/api/substack/posts",
    params=params,
    headers={"X-API-Key": API_KEY},
    timeout=60,
)
response.raise_for_status()
data = response.json()

for item in data.get("posts", []):
    print(" | ".join(str(item.get(k)) for k in ['title', 'published_at', 'likes', 'url']))
