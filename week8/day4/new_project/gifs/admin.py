from django.contrib import admin
from .models import Gif
from .models import Category
# Register your models here.

admin.site.register(Gif)
admin.site.register(Category)
