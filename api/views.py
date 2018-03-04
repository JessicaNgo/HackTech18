from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *


class FoodPictureViewSet(viewsets.ModelViewSet):
    queryset = FoodPicture.objects.all()
    serializer_class = FoodPictureSerializer


class UserFoodProfileViewSet(viewsets.ModelViewSet):
    queryset = UserFoodProfile.objects.all()
    serializer_class = UserFoodProfileSerializer


