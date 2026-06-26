import cloudscraper
from bs4 import BeautifulSoup
import json

BASE_URL = "https://steamrip.com"

scraper = cloudscraper.create_scraper()

def scrap(url):
    return BeautifulSoup(scraper.get(url).text, 'html.parser')

games_list_page = scrap(f'{BASE_URL}/games-list-page/')

games = []

for game_page_url in games_list_page.find_all("li", {"class": "az-list-item"}):

    game_name = game_page_url.find("a").string
    game_link = BASE_URL + game_page_url.find("a").get("href")

    games.append({
        "game": game_name,
        "link": game_link
    })

with open('data.json', 'w', encoding='utf-8') as jfile:
    json.dump(games, jfile, indent=4, ensure_ascii=False)