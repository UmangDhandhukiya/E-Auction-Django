from django.db import models
from django.utils import timezone
from datetime import timedelta

def get_auction_end_time():
    return timezone.now() + timedelta(days=1)

class image(models.Model):
    image = models.ImageField(upload_to="product_images/")
    caption = models.CharField(max_length=100)
    des = models.TextField()
    auction_end_time = models.DateTimeField(default=get_auction_end_time)

    def __str__(self):
        return self.caption

class contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=10)
    msg = models.CharField(max_length=122)

class orderlist(models.Model):
    caption = models.CharField(max_length=100)
    des = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100)
    email = models.CharField(max_length=90)

    def __str__(self):
        return self.caption
