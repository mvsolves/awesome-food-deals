from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, primary_key=False)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

# Create your models here.
class Deal(models.Model):
    deal_name = models.CharField(max_length=30)
    favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.deal_name


class Restaurant(models.Model):
    deals = models.ManyToManyField(Deal, related_name="deals")
    rest_name = models.CharField(max_length=30)
    rest_location = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.rest_name + " at " + self.rest_location
