from django.db import models
from django.contrib.auth.models import User



class FoodPicture(models.Model):

    # this feature vectors will essentially be a percentage ranking of all the kinds of foods that classification
    # guesses it falls under
    feature_vector = models.TextField(null=True)
    latitude =  models.FloatField()
    longitude = models.FloatField()


class FoodPreferenceElement(models.Model):
    user = models.ForeignKey(UserFoodProfile, on_delete=models.CASCADE)
    classification = models.CharField()
    value = models.FloatField()

    class Meta:
        unique_together=('user', 'classification')


class UserFoodProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # by using cos similarity of these children to another user - rank similarities
    # fuckit, just take cos similarity for all other users, give back top 10
    # alternative:
    #  userfoodprofile.foodpreferenceelement_set.values_list('classification') , sort and then take top 10 and
    # look for all other users with top 10
    # otheruserfoodprofile.foodpreferenceelement_set.values

    # use this to add or subtract from food preference
    food_pictures_liked = models.ManyToManyField(FoodPicture, related_name='user_likes')
    food_pictures_hated = models.ManyToManyField(FoodPicture, related_name='user_hates')
    latitude = models.FloatField()
    longitude = models.FloatField()





