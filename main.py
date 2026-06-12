from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
def confirmation():
    user_input = input("Press enter, if done. Else wait for it to finish!")
    if user_input:
        quit       

def scrape(LINK):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(LINK)
        raw_html = page.content()        
        print("Wait until the Google maps opens and everything loads!!!")
        soup = BeautifulSoup(raw_html, 'html.parser')
        confirmation()
        page.wait_for_selector("div[class*='Nv2PK']", state="visible", timeout=10000)
        page.click("div[class*='Nv2PK']")
        info_row = soup.find('div', class_='rogA2c')
        if info_row:
            phone_number = info_row.find('div')
            print(phone_number)
        time.sleep(10000)
        browser.close()

link = "https://www.google.com/maps/search/Pizza+Katerini"
if __name__ == "__main__":
    scrape(link)