from typing import Text
from django.db import models


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    specialization = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    date = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)


def insert(specialization, name, date, price):
    order = Order()
    order.specialization = specialization
    order.name = name
    order.date = date
    order.price = price
    order.save()
