from django.shortcuts import (render, redirect,
                              HttpResponseRedirect,
                              get_object_or_404)

from .forms import user_registration_form, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import blog_post
from .models import Bookmark

# Create your views here.


# View for user registrations
def register(request):
    if request.method == 'POST':
        form = user_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Your account has been created! Login now.')
            # page is redirected to login page
            return redirect('login')
    else:
        form = user_registration_form()

    return render(request, 'user_account/register.html', {'form': form})


# View for user profile update
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'user_account/profile.html', context)


# View to bookmark a post
@login_required
def add_bookmark(request, post_id):
    post = get_object_or_404(blog_post, id=post_id)
    Bookmark.objects.get_or_create(user=request.user, post=post)
    return redirect('post-detail', pk=post.id)


# View to remove bookmark from a post
@login_required
def remove_bookmark(request, post_id):
    post = get_object_or_404(blog_post, id=post_id)
    Bookmark.objects.filter(user=request.user, post=post).delete()
    return redirect('post-detail', pk=post.id)


# View to display all the bookmarks for a user
@login_required
def bookmarked_posts(request):
    bookmarks = Bookmark.objects.filter(
                user=request.user).select_related('post')
    return render(request,
                  'user_account/bookmarked_posts.html',
                  {'bookmarks': bookmarks})
