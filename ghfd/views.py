

#chapter3
# from django.http import HttpResponse
#def index(request):
    #return HttpResponse("Rango says hey there partner!<a href='/ghfd/about/'>About</a>")
#def about(request):
 #   return HttpResponse("Rango says here is the about page. <a href='/ghfd/'>Index</a>")

from django.shortcuts import render
from ghfd.models import Category, Page, UserProfile, Role, Cart, Order, Food, Review, Restaurant, Rating
from ghfd.forms import CategoryForm
from django.shortcuts import redirect
from django.urls import reverse
from ghfd.forms import PageForm
from django.contrib.auth.decorators import login_required
from ghfd.forms import UserForm, UserProfileForm
from datetime import datetime

def index(request):
    visitor_cookie_handler(request)
    return render(request, 'ghfd/index.html')

def about(request):
    context_dict = {}
    context_dict['visits'] = request.session['visits']
    
    visitor_cookie_handler(request)
    return render(request, 'ghfd/about.html', context=context_dict)

def cart(request):
    visitor_cookie_handler(request)
    return render(request, 'ghfd/cart.html')

def my_account(request):
    visitor_cookie_handler(request)
    return render(request, 'ghfd/my_account.html')

def restaurants(request):
    restaurant_list = Restaurant.objects.order_by('-views')

    context_dict = {}
    context_dict['restaurants'] = restaurant_list

    visitor_cookie_handler(request)
    return render(request, 'ghfd/restaurants.html', context=context_dict)

def show_restaurant(request, restaurant_name_slug):
    context_dict = {}

    try:
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)

        context_dict['restaurant'] = restaurant
    except Restaurant.DoesNotExist:
        context_dict['restaurant'] = None

    return render(request, 'ghfd/restaurant.html', context=context_dict)

def menu(request, restaurant_name_slug):
    context_dict = {}

    try:
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)
        food_list = Food.objects.filter(restaurant_id=restaurant.id)

        context_dict['foods'] = food_list
        context_dict['restaurant'] = restaurant
    except Food.DoesNotExist:
        context_dict['foods'] = None
        context_dict['restaurant'] = None

    return render(request, 'ghfd/menu.html', context=context_dict)

def show_food(request, restaurant_name_slug, food_name_slug):
    context_dict = {}

    try:
        food = Food.objects.get(slug=food_name_slug)
        review_list = Review.objects.filter(food_id=food.id)
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)

        context_dict['food'] = food
        context_dict['reviews'] = review_list
        context_dict['restaurant'] = restaurant
    except Restaurant.DoesNotExist:
        context_dict['foods'] = None
        context_dict['reviews'] = None
        context_dict['restaurant'] = None

    return render(request, 'ghfd/food.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'ghfd/category.html', context=context_dict)

@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('ghfd:index'))
        else:
            print(form.errors)

    return render(request, 'ghfd/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None

    if category is None:
        return redirect(reverse('ghfd:index'))

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('ghfd:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)  

    context_dict = {'form': form, 'category': category}
    return render(request, 'ghfd/add_page.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'ghfd/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



@login_required
def restricted(request):
    return render(request, 'ghfd/restricted.html')


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits


def introduction(request):
    visitor_cookie_handler(request)
    return render(request, 'ghfd/introduction.html')
def how_to_use(request):
    visitor_cookie_handler(request)
    return render(request, 'ghfd/how_to_use.html')
def out_team(request):
    visitor_cookie_handler(request)
    return render(request, 'ghfd/out_team.html')