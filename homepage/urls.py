from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('food-deals/', views.foodDeals, name='food-deals'),
    path('favorites/', views.favorites, name='favorites'),
    path('about/', views.about, name='about'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('restaurant/create', views.create_restaurant, name='create-rest'),
    path('login-required/', views.login_required_view, name='login-required'),
]


from django.urls import path
from . import views




