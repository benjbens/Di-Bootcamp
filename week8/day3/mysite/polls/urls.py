from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('index', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('show_email', views.show_email, name='show_email'),
]

# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route

