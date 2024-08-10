from django.db import models

# Create your models here.
class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    rewardsPoints = models.FloatField()