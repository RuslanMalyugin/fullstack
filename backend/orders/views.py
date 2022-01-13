from rest_framework import generics

from .models import Order
from .serializers import PostSerializersOrder


class OrderPostList(generics.ListAPIView):
    serializer_class = PostSerializersOrder
    queryset = Order.objects.all()


class OrderPostCreate(generics.CreateAPIView):
    serializer_class = PostSerializersOrder
