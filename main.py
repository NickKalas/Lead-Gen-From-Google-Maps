from playwright.sync_api import sync_playwright, TimeoutError
from bs4 import BeautifulSoup
from database import update_database
from check_for_valid import check      

def scrape(LINK, n_leads):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(LINK)
        page.wait_for_timeout(5000)
        
        listings = page.locator('//div[@role="article"]').all()

        for listing in listings[:n_leads]:
            
            counter = 1
            
            listing.click()
            page.wait_for_timeout(3000)
    
            name_attibute = '//h1[contains(@class, "DUwDvf")]' #Done
            address_xpath = '//button[@data-item-id="address"]//div[contains(@class, "fontBodyMedium")]'
            website_xpath = '//a[@data-item-id="authority"]//div[contains(@class, "fontBodyMedium")]'
            phone_number_xpath = '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]'

            if page.locator(name_attibute).count() > 0:
                biz_name = page.locator(name_attibute).inner_text()
            else:
                print(f"Something went wrong with the name of business {counter}...")
                biz_name = "N/A"

            # 3. Extract Address safely
            if page.locator(address_xpath).count() > 0:
                biz_adress = page.locator(address_xpath).first.inner_text()
            else:
                print(f"Something went wrong with the address of business {counter}...")
                biz_adress = "N/A"

            # 4. Extract Website safely
            if page.locator(website_xpath).count() > 0:
                # Pro Tip: Grabbing 'href' is more reliable than inner_text() for links
                biz_website = page.locator(website_xpath).inner_text()
            else:
                print(f"Something went wrong with the website of business {counter}...")
                biz_website = "N/A"

            # 5. Extract Phone safely
            if page.locator(phone_number_xpath).count() > 0:
                biz_phone = page.locator(phone_number_xpath).first.inner_text()
            else:
                print(f"Something went wrong with the phone of business {counter}...")
                biz_phone = 1111

            update_database(biz_name, biz_adress, biz_phone, "N/A", "N/A", biz_website)



        browser.close()

def make_link(query):
    link_template = "https://www.google.com/maps/search/"
    
    query = query.replace(" ", "+")
    link = link_template + query
    return link
