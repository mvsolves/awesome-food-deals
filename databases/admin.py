from django.contrib import admin
from .models import Restaurant, Deal, Customer, Location

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Deal)
admin.site.register(Customer)
admin.site.register(Location)
