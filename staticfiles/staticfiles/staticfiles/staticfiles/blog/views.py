from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import blog_post
from user_account.models import Bookmark

# Create your views here.


# View for Home page
def home(request):
    context = {
        'posts': blog_post.objects.all()
    }
    # Rendering the home html template with the post
    return render(request, 'blog/home.html', context)


# View for listing the blog posts
class post_list_view(ListView):
    model = blog_post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Order posts by the date posted
    paginate_by = 3  # Number of posts per page


# View for listsing the blog posts for a specific user
class user_post_list_view(ListView):
    model = blog_post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return blog_post.objects.filter(author=user).order_by('-date_posted')


# View to display a single post in detail
class post_detail_view(DetailView):
    model = blog_post
    context_object_name = 'post'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        # Checks if the user is logged in
        if self.request.user.is_authenticated:
            # checks if the post is bookmarked by the user
            context['is_bookmarked'] = Bookmark.objects.filter(
                user=self.request.user, post=post).exists()
        else:
            False
        return context


# View to create a new post
class post_create_view(LoginRequiredMixin, CreateView):
    model = blog_post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# View to update a existing blog post
class post_update_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = blog_post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Only if the current user is the author of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# View to delete a post
class post_delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = blog_post
    success_url = '/'

    # Only if the current user is the author of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# View for about page
def about(request):
    return render(request, 'blog/about.html')
