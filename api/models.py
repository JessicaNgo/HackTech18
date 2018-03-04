from django.db import models
from django.contrib.auth.models import User


class FoodClassification(models.Model):
    classification = models.TextField()
    probability_of_classification = models.FloatField()


class FoodPicture(models.Model):

    # this feature vectors will essentially be a percentage ranking of all the kinds of foods that classification
    # guesses it falls under
    image_url = models.URLField()
    tags = models.ManyToManyField(FoodClassification)
    latitude =  models.FloatField()
    longitude = models.FloatField()



class UserFoodProfile(models.Model):
    # TODO: create this model when user is created
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # by using cos similarity of these children to another user - rank similarities
    # fuckit, just take cos similarity for all other users, give back top 10

    # use this to add or subtract from food preference
    food_pictures_liked = models.ManyToManyField(FoodPicture, related_name='user_likes')
    food_pictures_hated = models.ManyToManyField(FoodPicture, related_name='user_hates')
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)


class FoodPreferenceElement(models.Model):
    user = models.ForeignKey(UserFoodProfile, on_delete=models.CASCADE)
    classification = models.ForeignKey(FoodClassification, on_delete=models.CASCADE)
    user_preference_sum = models.FloatField()

    class Meta:
        unique_together=('user', 'classification')





