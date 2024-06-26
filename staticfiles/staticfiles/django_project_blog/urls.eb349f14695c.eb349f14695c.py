"""
URL configuration for django_project_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views as home_views
from user_account import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import (post_list_view, 
                    post_detail_view,
                    post_create_view,
                    post_update_view,
                    post_delete_view,
                    user_post_list_view)

urlpatterns = [
    path('', post_list_view.as_view(), name='blog-home'),
    path('user/<str:username>', user_post_list_view.as_view(), name='user-posts'),
    path('admin/', admin.site.urls),
    path('about/', home_views.about, name='blog-about'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user_account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_account/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('post/<int:pk>/', post_detail_view.as_view(), name='post-detail'),
    path('post/new/', post_create_view.as_view(), name='post-create'),
    path('post/<int:pk>/update/', post_update_view.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', post_delete_view.as_view(), name='post-delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)