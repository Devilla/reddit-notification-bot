import requests
from bs4 import BeautifulSoup

import time
import pygame

URL = "https://www.reddit.com/r/Pokemonexchange/new.json"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

def play_pokemon_intro():
    pygame.mixer.init()
    pygame.mixer.music.load("pokemon_intro.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

last_seen_id = None
while True:
    response = requests.get(URL, headers=HEADERS)
    data = response.json()
    if 'data' in data and 'children' in data['data'] and len(data['data']['children']) > 0:
        post = data['data']['children'][0]['data']
        if post.get('id') != last_seen_id:
            print("Title:", post.get('title'))
            print("Author:", post.get('author'))
            print("Link: https://reddit.com" + post.get('permalink'))
            print("Content:", post.get('selftext')[:200])
            print()
            play_pokemon_intro()
            last_seen_id = post.get('id')
        else:
            print("No new posts.")
    else:
        print("No recent posts found.")
    time.sleep(60)
