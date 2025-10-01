from load_django_bs4 import *
from parser_app.models import BrainItem

import re
import requests
from bs4 import BeautifulSoup

URL = "https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html"

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

BrainItem.objects.create(**item_info)

print(item_info)