from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser
from .models import Person, Post, ImageProfile

# takes a request, returns a response
person = Person.objects.filter(first_name="benji").first()


def index(request):
    context = {
        'page_title' : "Homepage",
        'user' : person
    }
    return render(request, 'posts/homepage.html', context)

def posts(request):
    context = {
        'user' : person,
# we retrieve the person variable (created outside of the function)
        'page_title' : "Posts",
        'posts' : Post.objects.filter(
            author__first_name=person.first_name,
            author__last_name=person.last_name)
    }

    return render(request, 'posts/posts.html', context)


def show_email(request):
    context = {
        'user' : person,
        'email' : person.email
    }
    return render(request, 'show_email.html', context)