# Generated by Django 2.0.2 on 2018-03-04 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_vector', models.TextField(null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserFoodProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_preference_vector', models.TextField(null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('food_pictures_hated', models.ManyToManyField(related_name='user_hates', to='api.FoodPicture')),
                ('food_pictures_liked', models.ManyToManyField(related_name='user_likes', to='api.FoodPicture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]