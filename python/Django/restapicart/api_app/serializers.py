from rest_framework import serializers
from .models import Shoppingcart

class Cartserializer(serializers.ModelSerializer):
    class Meta:
        model = Shoppingcart
        fields = "__all__"