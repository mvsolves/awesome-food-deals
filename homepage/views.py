from django.shortcuts import render
from databases.models import Restaurant, Deal, Location

# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def is_valid_queryparam(param):
    return param != '' and param is not None

def foodDeals(request):
    count = Restaurant.objects.count()
    allRestaurants = Restaurant.objects.all()
    allDeals= Deal.objects.all().values()
    allLocations = Location.objects.all().values()

    loc = request.GET.get('loc')
    deal = request.GET.get('deal')

    print(loc)
    print(deal)

    if is_valid_queryparam(loc):
        allRestaurants = allRestaurants.filter(rest_location__location_name = loc)

    if is_valid_queryparam(deal):
        allRestaurants = allRestaurants.filter(deals__deal_name = deal)

    return render(request, 'food-deals.html', {'varAllRestaurants': allRestaurants,
                                               'varAllDeals': allDeals,
                                               'varAllLocations': allLocations,
                                               'varTotalCount': count,
                                               })
def favorites(request):
    count = Restaurant.objects.count()
    allRestaurants = Restaurant.objects.all()
    allDeals= Deal.objects.all().values()
    return render(request, 'favorites.html', {'varAllRestaurants': allRestaurants,
                                               'varAllDeals': allDeals,
                                               'totalCount': count
                                               })

def about(request):
    return render(request, 'about.html', {})

def FAQ(request):
    return render(request, 'FAQ.html', {})
