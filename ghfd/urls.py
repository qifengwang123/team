from django.urls import path
from ghfd import views

app_name = 'ghfd'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path('restricted/', views.restricted, name='restricted'),
    path('introduction/', views.introduction, name='introduction'),
    path('how_to_use/', views.how_to_use, name='how_to_use'),
    path('out_team/', views.out_team, name='out_team'),
    path('cart/', views.cart, name='cart'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('<slug:restaurant_name_slug>/', views.show_restaurant, name='show_restaurant'),
    path('<slug:restaurant_name_slug>/menu/', views.menu, name='menu'),
    path('<slug:restaurant_name_slug>/menu/<slug:food_name_slug>', views.show_food, name='show_food'),

]