import re
from typing import reveal_type
import attr
import requests
from bs4 import BeautifulSoup

URL = "https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html"
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

responce = requests.get(URL).text
soup = BeautifulSoup(responce, features="html.parser")

item_info = {}


try:
    full_name = soup.find("h1").text.strip() # DONE
except:
    full_name = None

try:
    color = soup.find("a", attrs={"title":re.compile(r"Колір*")}).text # DONE
except:
    color = None

try:
    storage = soup.find("a", attrs={"title":re.compile(r"Вбудована пам'ять*")}).text # DONE
except:
    storage = None

try:
    seller = soup.find("a", attrs={"class":"svg-logo-gray"})["href"].split("/")[2] # DONE
except:
    seller = None

try:
    price = soup.find("div", attrs={"class":"container br-container-main br-container-prt"})["data-price"] # DONE
except:
    price = None

try:
    discount_price = soup.find("span", attrs={"class":"red-price"}).text.strip() # DONE
except:
    discount_price = None

try:
    item_id = soup.find("div", attrs={"class":"container br-container-main br-container-prt"})["data-code"] # DONE
except:
    item_id = None

try:
    series = soup.find("div", attrs={"class":"container br-container-main br-container-prt"})["data-model"].split()[:2] # DONE
    series = series[0]+" "+series[1]
except:
    series = None

try:
    screen = soup.find("a", attrs={"title":re.compile("Діагональ екрану")}).text # DONE
except:
    screen = None

try:
    resolution = soup.find("a", attrs={"title":re.compile("Роздільна здатність екрану")}).text # DONE
except:
    resolution = None

try:
    photos_div = soup.find("div", class_="br-prs-f series-pictures-block")
    photos_img = photos_div.find_all("img", attrs={"title": re.compile(r"зображення \d")})
    photos_urls = [item["src"] for item in photos_img] # DONE
except:
    photos_urls = None
try:
    review_div = soup.find("div", class_="br-pt-rt-main-mark")
    review_count = review_div.find("span").text # DONE
except:
    review_count = None

try:
    all_specs = {}
    specs_chapters = soup.find_all("div", class_="br-pr-chr-item")
    for specs_chapter in specs_chapters:
        rows = specs_chapter.find("div").find_all("div")
        for row in rows:
            spans = row.find_all("span")
            key = spans[0].text.strip()
            val = " ".join(spans[1].text.split())
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

for key in item_info:
    print(f"{key}: {item_info[key]}")