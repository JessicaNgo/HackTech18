from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import *
from .serializers import *


# API for models
class FoodPictureViewSet(viewsets.ModelViewSet):
    queryset = FoodPicture.objects.all()
    serializer_class = FoodPictureSerializer


class UserFoodProfileViewSet(viewsets.ModelViewSet):
    queryset = UserFoodProfile.objects.all()
    serializer_class = UserFoodProfileSerializer


def parse_food_feature_vector_string(s):
    """ should parse the string into a dictionary of the classification, and its value"""
    return {}




# STRETCH TODO: make API endpoint that interfaces with YELP API where a POST request with the user ID and optionally,
# updated location (given in latitude/longitude) would trigger photos from yelp to go through to anna's
# classification/tagging, and create models for each of the photos and tags




# STRETCH TODO: make API endpoint that displays FoodPictures based on location, possibly post request with sorted by distance
# POST with USER ID, updated location (optional) and distance parameter (optional) default 5 miles

# TODO: make API endpoint for user swipes that takes USER ID, FOODPHOTO ID, and SWIPE(boolean)
@api_view(['POST'])
# API for user interface
def swipe_action(request):
    data = request.data
    user_pk = data['user_id']
    foodphoto_pk = data['foodphoto_id']
    swipe = data['swipe'] #boolean true or false

    foodphoto = FoodPicture.objects.get(pk=foodphoto_pk)

    for tag in foodphoto.tags.all():
        preference = FoodPreferenceElement.objects.get_or_create(classification__classification=tag.classification,
                                                          user__pk=user_pk)
        if swipe:
            preference.user_preference_sum = preference.user_preference_sum + tag.probability_of_classification
        else:
            preference.user_preference_sum = preference.user_preference_sum - tag.probability_of_classification

        preference.save()