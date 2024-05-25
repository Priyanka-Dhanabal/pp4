from django.db import models
from django.contrib.auth.models import User
from blog.models import blog_post
from PIL import Image
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Model for user proflies
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField(_("Profile Image"), null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


# Model for bookmarks
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(blog_post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # user can bookmark only once
    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user.username} bookmarked {self.post.title}'
