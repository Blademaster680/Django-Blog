from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
posts = [
    {
        'author': 'Blade',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '23 February, 2020'
    },
    {
        'author': 'Blade',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '24 February, 2020'
    },
    {
        'author': 'Blade',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': '25 February, 2020'
    }
]


def home(request):
    # Create a Dictionary
    context = {
        'posts': Post.objects.all()
    }

    # Passing the posts dictionary data into the home.html
    return render(request, 'blog/home.html', context)


def about(request):
    #title = 'About Us'
    return render(request, 'blog/about.html')