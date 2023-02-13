from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('food-deals/', views.foodDeals, name='food-deals'),
    path('search/', views.search, name='search'),
    path('favoites/', views.favorites, name='favorites'),
    path('about/', views.about, name='about'),
    path('FAQ/', views.FAQ, name='FAQ'),
]


