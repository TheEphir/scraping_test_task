"""
Collect data about Iphone from brain.com.ua 
"""

from load_django import *
from parser_app.models import BrainItem

import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

START_URL = "https://brain.com.ua/"
SEARCH_ITEM = "Apple iPhone 15 128GB Black"

ITEM_SPECS_XPATH = {
    "full_name":'//div[@class="title"]/h1',
    "color":'//a[contains(@title, "Колір")]',
    "storage":'//a[contains(@title, "Вбудована пам")]',
    "seller":'//div[@class="logo"]/a',
    "price":'//div[@class="br-pr-np"]/div/span',
    "discount_price":'//span[@class="red-price"]',
    "photos":'//div[contains(@class, "slick-slide slick")]/img',
    "item_id":'//div[@class="container br-container-main br-container-prt"][contains(data-code,"")]',
    "review_count":'//div[@class="br-pt-rt-main-mark"]//a[@href="#reviews-list"]/span',
    "series":'//div[@class="container br-container-main br-container-prt"][contains(data-model,"")]',
    "screen":'//a[contains(@title, "Діагональ")]',
    "resolution":'//a[contains(@title, "Роздільна здатність екрану")]',
    "all_specs":'//div[@class="br-pr-chr-item"]/div/div',
}


def get_item_info(driver_path:str) -> dict[str:any]:
    """should make it with json format"""
    
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(START_URL)
    except:
        print("error from start")
        
    try:
        search_xpath = '//div[@class="header-bottom"]//form/input[@class="quick-search-input"][@placeholder="Знайти..."]'
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
    except TimeoutException:
        driver.quit()
        print("Timeout error")

    search_field = driver.find_element(By.XPATH, search_xpath)
    search_field.send_keys(SEARCH_ITEM)
    search_field.send_keys(Keys.ENTER)

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="search-result"]')))
    except TimeoutException:
        driver.quit()
        print("Timeout error")

    first_item_xpath = '//div[@class="view-grid tab-pane row br-row br-flex active"]/div[1]//div[@class="br-pp-img br-pp-img-grid"]/a'
    first_item_url = driver.find_element(By.XPATH, first_item_xpath).get_attribute("href")

    driver.get(first_item_url)

    try:
        characteristics_xpath = '//div[@id="br-characteristics"]'
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, characteristics_xpath)))
    except TimeoutException:
        driver.quit()
        print("Timeout error")
        

    try:
        full_name = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["full_name"]).text
    except:
        full_name = None

    try:
        color = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["color"]).get_attribute("text")
    except:
        color = None

    try:
        storage = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["storage"]).get_attribute("text")
    except:
        storage = None

    try:
        seller = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["seller"]).get_attribute("href").split("/")[2]
    except:
        seller = None

    try:
        price = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["price"]).text
    except:
        price = None

    try:
        discount_price = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["discount_price"]).text
    except:
        discount_price = None

    try:
        photos_images = driver.find_elements(By.XPATH, ITEM_SPECS_XPATH["photos"])
        photos_urls = [item.get_attribute("src") for item in photos_images]
    except:
        photos_urls = None

    try:
        item_id = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["item_id"]).get_attribute("data-code")
    except:
        item_id = None

    try:
        review_count = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["review_count"]).text
    except:
        review_count = None

    try:
        raw_series = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["series"]).get_attribute("data-model").split(" ")
        series = raw_series[0] + " " + raw_series[1]
    except:
        series = None

    try:
        screen = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["screen"]).get_attribute("text")
    except:
        screen = None

    try:
        resolution = driver.find_element(By.XPATH, ITEM_SPECS_XPATH["resolution"]).get_attribute("text")
    except:
        resolution = None

    all_specs = {}
    # this won't work proper idk why, path working ok, but still get empty keys and values...
    try:
        specs_chapters = driver.find_elements(By.XPATH, '//div[@class="br-pr-chr-item"]')
        for chapter in specs_chapters:
            rows = chapter.find_elements(By.TAG_NAME, "div")
            for row in rows:
                spans = row.find_elements(By.TAG_NAME, "span")
                key = spans[0].text
                val = spans[1].text
                all_specs.update({key:val})
    except:
        all_specs = None
    
    driver.quit()
    
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


def get_driver_path():
    return os.getcwd()+'/chromedriver.exe'


data = get_item_info(get_driver_path())
print(data)
BrainItem.objects.create(**data)
