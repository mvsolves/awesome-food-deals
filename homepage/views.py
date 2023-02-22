from django.shortcuts import render
from databases.models import Restaurant, Deal

from databases.models import Restaurant

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def foodDeals(request):
    count = Restaurant.objects.count()
    allRestaurants = Restaurant.objects.all()
    allDeals= Deal.objects.all().values()
    return render(request, 'food-deals.html', {'varAllRestaurants': allRestaurants,
                                               'varAllDeals': allDeals,
                                               'totalCount': count
                                               })
def favorites(request):
    return render(request, 'favorites.html', {})

def about(request):
    return render(request, 'about.html', {})

def FAQ(request):
    return render(request, 'FAQ.html', {})
