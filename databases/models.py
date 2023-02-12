from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deal(models.Model):
    deal_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.deal_name

class Restaurant(models.Model):
    deals = models.ManyToManyField(Deal, related_name="deals")
    rest_name = models.CharField(max_length=30)
    rest_location = models.CharField(max_length=30)
    user = models.ManyToManyField(User, primary_key=False)

    def __str__(self) -> str:
        return self.rest_name + " at " + self.rest_location
