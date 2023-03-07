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
    path('fav/add_to_favorites/<int:id>', views.add_to_favorites, name='favorite_rest'),
    path('fav/remove_from_favorites/<int:id>', views.remove_from_favorites, name='unfavorite_rest')
]


from django.urls import path
from . import views




