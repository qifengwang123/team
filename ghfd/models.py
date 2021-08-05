from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Role(models.Model):
    ID_MAX_LENGTH = 32
    NAME_MAX_LENGTH = 64
    DESCRIPTION_MAX_LENGTH = 256

    id = models.CharField(max_length=ID_MAX_LENGTH, unique=True, primary_key=True)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    name = models.CharField(max_length=NAME_MAX_LENGTH)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    ID_MAX_LENGTH = 32
    TEXT_MAX_LENGTH = 64
    DESCRIPTION_MAX_LENGTH = 256

    id = models.CharField(max_length=ID_MAX_LENGTH, unique=True, primary_key=True)
    name = models.CharField(max_length=TEXT_MAX_LENGTH)
    address = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    phone = models.CharField(max_length=TEXT_MAX_LENGTH)
    views = models.IntegerField(default=0)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    average_rating = models.FloatField(default=0)
    manager_id = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Food(models.Model):
    ID_MAX_LENGTH = 32
    NAME_MAX_LENGTH = 64
    DESCRIPTION_MAX_LENGTH = 256

    id = models.CharField(max_length=ID_MAX_LENGTH, unique=True, primary_key=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    price = models.IntegerField()
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Food, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Cart(models.Model):
    ID_MAX_LENGTH = 32

    food_id = models.ManyToManyField(Food)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Cart: " + self.user_id

class Order(models.Model):
    ID_MAX_LENGTH = 32
    STATUS_MAX_LENGTH = 64

    id = models.CharField(max_length=ID_MAX_LENGTH, unique=True, primary_key=True)
    price = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=STATUS_MAX_LENGTH)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    food_id = models.ManyToManyField(Food)

    def __str__(self):
        return self.id

class Review(models.Model):
    ID_MAX_LENGTH = 32
    CONTENT_MAX_LENGTH = 256

    id = models.CharField(max_length=ID_MAX_LENGTH, unique=True, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.CharField(max_length=CONTENT_MAX_LENGTH)

    def __str__(self):
        return self.id

class Rating(models.Model):
    ID_MAX_LENGTH = 32

    id = models.CharField(max_length=ID_MAX_LENGTH, unique=True, primary_key=True)
    rating = models.FloatField()
    taste = models.IntegerField()
    speed = models.IntegerField()
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id