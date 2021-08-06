from django.urls import path
from ghfd import views

app_name = 'ghfd'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('introduction/', views.introduction, name='introduction'),
    path('how_to_use/', views.how_to_use, name='how_to_use'),
    path('out_team/', views.out_team, name='out_team'),
    path('cart/', views.get_cart, name='cart'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('my_account/', views.my_account, name='my_account'),
    path('<slug:restaurant_name_slug>/', views.show_restaurant, name='show_restaurant'),
    path('<slug:restaurant_name_slug>/menu/', views.menu, name='menu'),
    path('<slug:restaurant_name_slug>/menu/<slug:food_name_slug>', views.show_food, name='show_food'),
    path('add_to_cart/<int:food_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/remove_from_cart/<int:food_id>', views.remove_from_cart, name='remove_from_cart'),
]