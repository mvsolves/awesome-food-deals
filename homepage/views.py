from django.shortcuts import render, redirect, get_object_or_404
from databases.models import Restaurant, Deal, Location, Customer
from .forms import RestaurantForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.http import HttpResponseNotFound


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
    search = request.GET.get('search-bar')

    if is_valid_queryparam(loc):
        allRestaurants = allRestaurants.filter(rest_location__location_name = loc)

    if is_valid_queryparam(deal):
        allRestaurants = allRestaurants.filter(deals__deal_name = deal)

    if is_valid_queryparam(search):
        allRestaurants = allRestaurants.filter(rest_name__icontains = search)

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

def login_required_view(request):
    return render(request, 'login_required.html')

@login_required(login_url='login-required')
def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_restaurant = form.save(commit=False)
            new_restaurant.save()

            # Get the selected location and save it to the restaurant object
            location_id = int(request.POST.get('rest_location'))
            location = Location.objects.get(pk=location_id)
            new_restaurant.location = location
            new_restaurant.save()

            # Get the selected deals and save them to the restaurant object
            deals = request.POST.getlist('deals')
            for deal_id in deals:
                deal = Deal.objects.get(pk=int(deal_id))
                new_restaurant.deals.add(deal)

            request.user.customer.favorite_rest.add(new_restaurant)
            return redirect('food-deals')
    else:
        form = RestaurantForm()
    return render(request, 'create-rest.html', {'form': form})

@login_required(login_url='login-required')
def add_to_favorites(request, id):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return HttpResponseNotFound('No Customer matches the given query.')

    if customer.favorite_rest.filter(id=id).exists():
        customer.favorite_rest.remove(id)
    else:
        customer.favorite_rest.add(id)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
