from django.shortcuts import render
from django.views.generic import (ListView, DetailView, 
                                    CreateView)
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


class post_create_view(CreateView):
    model = blog_post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html')