# from brain_selenium_project.parser_app.models import BrainItem
# from parser_app.models import BrainItem

# item_info = {
#     "full_name":"test name",
#     "color":"red",
#     "storage":"128 Gb",
#     "seller":"seller",
#     "price":123,
#     "discount_price": None,
#     "photos":["url0","url1","url2","url3"],
#     "item_id":"UD12334",
#     "review_count":None,
#     "series":"series123",
#     "screen":"6.1'",
#     "resolution":"123x654",
#     "all_specs":{
#         "helo":"specs",
#         "helo1":"specs1",
#         "helo2":"specs2",
#     },
# }

# BrainItem.objects.create(**item_info)

import json
import requests

from modules.selenium_scraper import get_item_info, get_driver_path

data = json.dumps(get_item_info("E:\projects\scraping_test_task\modules\chromedriver.exe"))

print(data)
print(json.loads(requests.post("http://localhost:8000/items/create/", data=data).json()))