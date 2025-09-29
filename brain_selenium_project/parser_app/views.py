import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from parser_app.models import BrainItem


# from ...modules.selenium import selenium_scraper
# Create your views here.
@csrf_exempt
def item_create(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            item = BrainItem.objects.create(**data)
            return JsonResponse({"id": item.item_id, "name":item.full_name}, status=201)
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({"error":"Invalid data", "data": data, "item":item}, status=400)
    return JsonResponse({"error":"Method not allowed"}, status=405)


def item_list(request):
    if request.method == "GET":
        items = BrainItem.objects.all()
        res = []
        for elem in items:
            item_info = {
                "id":elem.item_id,
                "full_name":elem.full_name,
                "color":elem.color,
                "storage":elem.storage,
                "seller":elem.seller,
                "price":elem.price,
                "discount_price":elem.discount_price,
                "photos":elem.photos,
                "item_id":elem.item_id,
                "review_count":elem.review_count,
                "series":elem.series,
                "screen":elem.screen,
                "resolution":elem.resolution,
                "all_specs":elem.all_specs,
            }
            res.append(item_info)
        return JsonResponse({"items":res}, status=200)

    return JsonResponse({"error":"Method not allowed"}, status=404)
        