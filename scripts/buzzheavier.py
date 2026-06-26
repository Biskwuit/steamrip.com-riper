import cloudscraper
from bs4 import BeautifulSoup
from bhdownloader import get_file_info, download

BASE_URL = "https://buzzheavier.com"

scraper = cloudscraper.create_scraper(interpreter='js2py', delay=10)

soup = BeautifulSoup(scraper.get(f"{BASE_URL}/cwe2hrbif4al").text, 'html.parser')

dwnlink = soup.find("a", {"class": "download-btn"}).get("hx-get")

print(f'{BASE_URL}{dwnlink}')

with scraper.get(f'{BASE_URL}{dwnlink}', stream=True) as r:
    r.raise_for_status()
    with open("Mario Kart 64 (axekin.com).z64", "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)