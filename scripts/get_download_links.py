import cloudscraper
from bs4 import BeautifulSoup
import json

BASE_URL = "https://steamrip.com"

scraper = cloudscraper.create_scraper()

def scrap(url):
    return BeautifulSoup(scraper.get(url).text, 'html.parser')

def get_uploader_name(url):
    return url.split('/')[2].split('.')[0]

def ident_game_name(name):
    return name.split(' Free Download')[0]

games_list_page = scrap(f'{BASE_URL}/games-list-page/')

games = {"games":[]}
downloads = {}

# for game_page_url in games_list_page.find_all("li", {"class": "az-list-item"}):

#     game_name = game_page_url.find("a").string
#     game_link = BASE_URL + game_page_url.find("a").get("href")

#     games.append({
#         "game": game_name,
#         "link": game_link
#     })

# with open('data.json', 'w', encoding='utf-8') as jfile:
#     json.dump(games, jfile, indent=4, ensure_ascii=False)

game_infos = games_list_page.find("li", {"class": "az-list-item"})
game_page = scrap(f'{BASE_URL}{game_infos.find("a").get("href")}')

game_name = game_infos.find("a").string

for download_links in game_page.find_all("a", string="DOWNLOAD HERE"):

    host = get_uploader_name(download_links.get("href"))
    link = f'https:{download_links.get("href")}'

    downloads.setdefault(host, []).append(link)

cpu = game_page.find("strong", string="Processor:").find_parent("li").get_text().split('Processor: ')[1]
directx = game_page.find("strong", string="DirectX").find_parent("li").get_text().split('DirectX ')[1]
gpu = game_page.find("strong", string="Graphics:").find_parent("li").get_text().split('Graphics: ')[1]
os = game_page.find("strong", string="OS:").find_parent("li").get_text().split('OS: ')[1]


games["games"].append({
    "dirlink": f'{BASE_URL}{game_infos.find("a").get("href")}',
    "download_links": downloads,
    "game": ident_game_name(game_name),
    "minReqs": {
        "cpu" : cpu,
        "directx" : directx,
        "gpu" : gpu,
        "os" : os
        }
})

with open("index.html", "w") as html:
    htmlwrite(soup)