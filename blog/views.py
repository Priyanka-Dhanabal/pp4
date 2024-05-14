from django.shortcuts import render
from .models import blog_post

# Create your views here.

def home(request):
    context = {
        'posts': blog_post.objects.all()
    }
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')