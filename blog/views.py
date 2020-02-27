from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .forms import PostCreateForm, PostUpdateForm

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


class PostListView(ListView):
    model = Post
    # template_name = <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    # template_name = <app>/<model>_<viewtype>.html
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        # Get the username from the URL to filter their posts
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    #title = 'About Us'
    return render(request, 'blog/about.html')