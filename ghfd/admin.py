from django.contrib import admin
from ghfd.models import Category, Page, UserProfile, Role, Order, Food, Review, Restaurant, Rating
from cart.models import Item

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class RestaurantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class FoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin) 
admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Rating)
admin.site.register(Item)
