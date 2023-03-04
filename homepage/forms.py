from django import forms
from databases.models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('rest_name', 'rest_location', 'deals')
