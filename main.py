from playwright.sync_api import sync_playwright, TimeoutError
from bs4 import BeautifulSoup
from database import update_database
import random
def get_info(page, name_xpath, address_xpath, website_xpath, phone_number_xpath, average_reviews_xpath, reviews_xpath, counter):
    if page.locator(name_xpath).count() > 0:
        biz_name = page.locator(name_xpath).inner_text()
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
    if page.locator(average_reviews_xpath).count() > 0:
        biz_avr_reviews = page.locator(average_reviews_xpath).first.inner_text()
    else:
        print(f"Something went wrong with the review average of business {counter}...")
        biz_avr_reviews = "N/A"
    if page.locator(reviews_xpath).count() > 0:
        reviews = page.locator(reviews_xpath).first.inner_text()
    else:
        print(f"Something went wrong with the reviews of business {counter}...")
        reviews = "N/A"

    return biz_name, biz_adress, biz_website, biz_phone, biz_avr_reviews, reviews

def scrape(LINK, n_leads):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        accept_all = page.locator('//button[@jsname="tWT92d"]')
        page.goto(LINK)
        page.evaluate("window.scrollBy(0, 800);")
        page.wait_for_timeout(random.randint(0,1000))
        accept_all.first.click()
        page.wait_for_timeout(random.randint(7500,9000))
        
        listings = page.locator('//div[@role="article"]').all()
        if listings:
            for listing in listings[:n_leads]:
                
                counter = 1
                
                listing.scroll_into_view_if_needed()
                listing.click()
                page.wait_for_timeout(random.randint(3500,4000))

                #These are all the xpaths that we will need to correctly get our information
                name_xpath = '//h1[contains(@class, "DUwDvf")]'
                address_xpath = '//button[@data-item-id="address"]//div[contains(@class, "fontBodyMedium")]'
                website_xpath = '//a[@data-item-id="authority"]//div[contains(@class, "fontBodyMedium")]'
                phone_number_xpath = '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]'
                average_reviews_xpath = '//div[@class="F7nice " or contains(@class, "F7nice")]//span[@aria-hidden="true"]'
                reviews_xpath = '//div[@class="F7nice " or contains(@class, "F7nice")]//span[contains(@aria-label, "αξιολογήσεις") or contains(@aria-label, "reviews")]'

                biz_name, biz_adress, biz_website, biz_phone, reviews, biz_avr_reviews = get_info(page, name_xpath, address_xpath, website_xpath, phone_number_xpath, average_reviews_xpath, reviews_xpath, counter)
                
                update_database(biz_name, biz_adress, biz_phone, reviews, biz_avr_reviews, biz_website)



            browser.close()
        else:
            print("No listings were found... Try another search query!")
            quit

def make_link(query):
    link_template = "https://www.google.com/maps/search/"
    
    query = query.replace(" ", "+")
    link = link_template + query
    return link
