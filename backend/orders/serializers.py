from django.db.models import fields
from rest_framework import serializers
from .models import Order


class PostSerializersOrder(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
