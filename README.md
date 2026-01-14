# Reddit Notification Bot

This bot monitors the latest posts on the [r/Pokemonexchange](https://www.reddit.com/r/Pokemonexchange/) subreddit and prints new post info every minute.

## Features
- Scrapes new posts from Reddit using the JSON endpoint
- Prints post title, author, link, and content
- Avoids duplicate notifications
- Modular for extension (Discord/email/webhook support possible)

## Requirements
- Python 3.7+
- Reddit does **not** require an API key for basic read-only scraping via the JSON endpoint
- Packages:
    - `requests`
    - `beautifulsoup4`

## Setup

### 1. Clone this repo
```
git clone <your-repo-url>
cd reddit-notification-bot
```

### 2. Create & activate a Python virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```
pip install requests beautifulsoup4
```

### 4. Run the bot
```
python bot.py
```

The script will check r/Pokemonexchange for new posts every 60 seconds, printing details for new ones as they appear.

## Customization
- To send Discord notifications: Add code to POST to a Discord webhook whenever a new post is found. (Ask for sample code if you need this!)
- To change the subreddit, edit the `URL` in `bot.py`.

## Notes
- The bot uses Reddit's public JSON endpoints; if scraping Reddit for large/production use, consider their API or rate limits.
- Stop the script at any time with `Ctrl+C`.

## License
MIT (or specify your preferred license)
