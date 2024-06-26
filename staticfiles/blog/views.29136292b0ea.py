from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView, 
                                DetailView, 
                                CreateView,
                                UpdateView,
                                DeleteView)
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
    paginate_by = 3


class user_post_list_view(ListView):
    model = blog_post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return blog_post.objects.filter(author=user).order_by('-date_posted')


class post_detail_view(DetailView):
    model = blog_post


class post_create_view(LoginRequiredMixin, CreateView):
    model = blog_post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class post_update_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = blog_post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class post_delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = blog_post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html')