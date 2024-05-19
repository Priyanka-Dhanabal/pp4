from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import blog_post

# Create your views here.

def home(request):
    context = {
        'posts': blog_post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class post_list_view(ListView):
    model = blog_post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class post_detail_view(DetailView):
    model = blog_post


def about(request):
    return render(request, 'blog/about.html')