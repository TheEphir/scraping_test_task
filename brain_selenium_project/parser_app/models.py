from django.db import models

# Create your models here.
class BrainItem(models.Model):
    full_name = models.CharField(max_length=256)
    color = models.CharField(max_length=25)
    storage = models.CharField(max_length=20)
    seller = models.CharField(max_length=25)
    price = models.IntegerField()
    discount_price = models.IntegerField(null=True, blank=True)
    photos = models.TextField()
    item_id = models.CharField(max_length=25)
    review_count = models.IntegerField(null=True, blank=True)
    series = models.CharField(max_length=256)
    screen = models.CharField(max_length=10)
    resolution = models.CharField(max_length=15)
    all_specs = models.TextField(null=True, blank=True)
    
    # 01234567890123456789012345 = 25 chars
    