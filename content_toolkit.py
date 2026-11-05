#!/usr/bin/env python3
"""
AI Social Media Content Toolkit
Drafts original content, formats for X/Twitter and Facebook Reels,
generates captions/hashtags, and performs quality checks.
No automatic publishing.
"""

import os
import json
from typing import Dict, List

def draft_content(topic: str, tone: str = "professional", length: str = "medium") -> str:
    """Placeholder for AI-assisted drafting. Use env vars for real API keys."""
    base = f"Draft post about {topic} in {tone} tone ({length} length)."
    return base + " (Integrate OpenAI or similar via OPENAI_API_KEY)"

def format_for_x(text: str, max_length: int = 280) -> str:
    """Format for X/Twitter."""
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    return text

def format_for_reels(text: str, title: str = "") -> Dict:
    """Generate Facebook Reels metadata."""
    return {
        "title": title or text[:60],
        "description": text[:150],
        "hashtags": generate_hashtags(text.split()[0] if text else "AI"),
        "duration_suggestion": "15-30s",
        "aspect_ratio": "9:16"
    }

def generate_hashtags(topic: str) -> List[str]:
    clean = topic.replace(" ", "")
    return [f"#{clean}", "#Web3", "#AI", "#Automation", "#BuildInPublic"]

def quality_check(text: str, platform: str = "x") -> Dict:
    score = 0.8 if len(text) > 50 else 0.5
    if platform == "reels" and len(text) < 100:
        score += 0.1
    return {
        "length": len(text),
        "has_hashtags": "#" in text,
        "score": min(1.0, score),
        "platform": platform,
        "notes": "Manual review recommended before posting. No auto-publish."
    }

def main():
    topic = "AI agents in Web3"
    draft = draft_content(topic)
    x_post = format_for_x(draft)
    reels = format_for_reels(draft, "AI Agents Web3")
    hashtags = generate_hashtags(topic)
    check_x = quality_check(x_post, "x")
    check_reels = quality_check(draft, "reels")
    
    output = {
        "draft": draft,
        "x_formatted": x_post,
        "reels_metadata": reels,
        "hashtags": hashtags,
        "quality_x": check_x,
        "quality_reels": check_reels
    }
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
