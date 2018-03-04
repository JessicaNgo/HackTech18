from rest_framework import serializers
from .models import *


class UserFoodProfileSerializer(serializers.Serializer):
    class Meta:
        model = UserFoodProfile
        fields = '__all__'


class FoodPictureSerializer(serializers.Serializer):
    class Meta:
        model = FoodPicture
        fields = '__all__'