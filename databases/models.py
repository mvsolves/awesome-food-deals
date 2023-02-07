from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    rest_name = models.CharField(max_length=30)
    rest_location = models.CharField(max_length=30)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, primary_key=False)

    def __str__(self) -> str:
        return self.rest_name + " at " + self.rest_location

class Deal(models.Model):
    deal_name = models.CharField(max_length=30)
    rest = models.ManyToManyField(Restaurant, related_name='restaurant_deals')

    def __str__(self) -> str:
        return self.deal_name
