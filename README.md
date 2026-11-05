# AI Social Media Content Toolkit

Modular Python tool for producing original social media content.

## Features

- AI-assisted content drafting (API key via environment variables, configurable length/tone)
- X/Twitter post formatting
- Facebook Reels metadata generation (title, description, aspect ratio)
- Caption and hashtag assistance
- Multi-platform content quality checks
- Optional API integrations
- Basic unit tests and CI workflow

**No automatic publishing** unless you explicitly implement and approve it.

## Installation

```bash
git clone https://github.com/demarco2016/ai-social-content-toolkit.git
cd ai-social-content-toolkit
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your keys if needed
```

## Usage

```bash
python content_toolkit.py
python -m unittest test_toolkit.py -v
```

Extend the functions to call real AI APIs using keys from `.env`.

## Disclaimer

Generated content should be reviewed before publishing. This is a starter toolkit.
