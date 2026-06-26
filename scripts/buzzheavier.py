import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time

options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Explicitly set Chrome binary location for Linux/Codespaces
options.binary_location = "/usr/bin/chromium-browser"

driver = uc.Chrome(options=options, use_subprocess=True)
driver.get("https://bzzhr.to/rcby3xmpgwb4")

# Wait for Cloudflare challenge to solve
time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)

driver.quit()   