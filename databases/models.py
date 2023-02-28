from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Deal(models.Model):
    deal_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.deal_name

class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.location_name

class Restaurant(models.Model):
    deals = models.ManyToManyField(Deal, related_name="deals")
    rest_name = models.CharField(max_length=30)
    rest_location = models.ForeignKey('Location', null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.rest_name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, primary_key=False)
    favorite_rest = models.ManyToManyField(Restaurant, related_name="restaurants")

    def __str__(self) -> str:
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customer.save()

