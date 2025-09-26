import time
import re
from playwright.sync_api import sync_playwright

from xpath import get_brain_com_ua_xpath

START_URL = "https://brain.com.ua/"
SEARCH_ITEM = "Apple iPhone 15 128GB Black"
ITEM_SPECS_XPATH = get_brain_com_ua_xpath()
TIMEOUT = 1000 # 1sec


def get_item_info():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.screenshot()
        page.goto(START_URL)
        
        time.sleep(1)
        search_field_xpath = '//div[@class="header-bottom"]//form/input[@class="quick-search-input"][@placeholder="Знайти..."]'
        try:
            search_field = page.locator(search_field_xpath)
        except:
            return
        
        search_field.fill(SEARCH_ITEM)
        search_field.press("Enter")
        
        time.sleep(1)

        first_item_xpath = '//div[@class="view-grid tab-pane row br-row br-flex active"]/div[1]//div[@class="br-pp-img br-pp-img-grid"]/a'
        first_item_url = page.locator(first_item_xpath).get_attribute("href")
        
        page.goto(first_item_url)
        time.sleep(1)
        
        try:
            full_name = page.locator(ITEM_SPECS_XPATH["full_name"]).text_content(timeout=TIMEOUT).strip() # DONE
        except:
            full_name = None
        try:
            color = page.locator(ITEM_SPECS_XPATH["color"]).text_content(timeout=TIMEOUT) # DONE
        except:
            color = None
        try:
            storage = page.locator(ITEM_SPECS_XPATH["storage"]).text_content(timeout=TIMEOUT) # DONE
        except:
            storage = None
        try:
            seller = page.locator(ITEM_SPECS_XPATH["seller"]).get_attribute(name="href").split("/")[2] # DONE
        except:
            seller = None
        
        try:
            # index 0 = because have found more than 1 match, and 0 is one that shown on site
            price = page.locator(ITEM_SPECS_XPATH["price"]).all()[0].text_content(timeout=TIMEOUT).strip() # DONE
        except:
            price = None
            
        try:
            discount_price = page.locator(ITEM_SPECS_XPATH["discount_price"]).text_content(timeout=TIMEOUT) # DONE
        except:
            discount_price = None
        
        try:
            photos_images = page.locator(ITEM_SPECS_XPATH["photos"]).all()
            photos_urls = [item.get_attribute("src") for item in photos_images] # DONE
        except:
            photos_urls = None
        
        try:
            # index 0 = because have found 2 matches, and 0 is one that shown on site
            item_id = page.locator(ITEM_SPECS_XPATH["item_id"]).all()[0].get_attribute("data-code") # DONE
        except:
            item_id = None
            
        try:
            review_count = page.locator(ITEM_SPECS_XPATH["review_count"]).text_content(timeout=TIMEOUT)
        except:
            review_count = None
        
        try:        
            # index 0 = because have found 2 matches, and 0 is one that shown on site
            raw_series = page.locator(ITEM_SPECS_XPATH["series"]).all()[0].get_attribute("data-model").split(" ")
            series = raw_series[0] + " " + raw_series[1] # DONE
        except:
            series = None
        
        try:
            screen = page.locator(ITEM_SPECS_XPATH["screen"]).text_content(timeout=TIMEOUT) # DONE
        except:
            screen = None

        try:
            resolution = page.locator(ITEM_SPECS_XPATH["resolution"]).text_content(timeout=TIMEOUT) # DONE
        except:
            resolution = None

        try:
            # That is so far as i can get
            all_specs = {}
            rows = page.locator(ITEM_SPECS_XPATH["all_specs"]).all()
            for row in rows:
                spans = row.locator("//span").all()
                key = spans[0].text_content().strip()
                val = re.sub(r"[^\w\s]", "", spans[1].text_content().strip().replace(u"\xa0", u"").replace(u"\n", u"")) # clear non-writable characters
                all_specs.update({key:val})
        except:
            all_specs = None
        
        
        item_info = {
            "full_name":full_name,
            "color":color,
            "storage":storage,
            "seller":seller,
            "price":price,
            "discount_price":discount_price,
            "photos":photos_urls,
            "item_id":item_id,
            "review_count":review_count,
            "series":series,
            "screen":screen,
            "resolution":resolution,
            "all_specs":all_specs,
        }
        
        return item_info


# get_item_info()

res = get_item_info()
for key in res:
    print(f"{key}: {res[key]}")
