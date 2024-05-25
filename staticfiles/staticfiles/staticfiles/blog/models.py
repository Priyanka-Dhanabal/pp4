from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.


# Model for posts
class blog_post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')

    # Returning the title of the post
    def __str__(self):
        return self.title

    # Redirects to the post's detail view
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
