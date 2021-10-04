from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import Cart,Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'name','added','last_update','dishs']
