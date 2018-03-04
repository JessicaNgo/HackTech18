from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import *


class UserFoodProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFoodProfile
        fields = '__all__'


class FoodPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPicture
        fields = '__all__'