import cloudscraper
from bs4 import BeautifulSoup

BASE_URL = "https://buzzheavier.com"

scraper = cloudscraper.create_scraper(interpreter='js2py', delay=10)

soup = BeautifulSoup(scraper.get(f"{BASE_URL}/1394jyvf41wq").text, 'html.parser')

if soup.find("p", {"class": "file-name"}):
    filename = soup.find("p", {"class": "file-name"}).get_text()
    print(filename)

if soup.find("a", {"class": "download-btn"}):
    dwnlink = soup.find("a", {"class": "download-btn"}).get("hx-get")
    print(f'{BASE_URL}{dwnlink}')
else:
    print('No File Found / Might be Rate Limited, retry.')

if (soup.find("a", {"class": "download-btn"}) and soup.find("p", {"class": "file-name"})):
    with scraper.get(f'{BASE_URL}{dwnlink}', stream=True) as r:
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)