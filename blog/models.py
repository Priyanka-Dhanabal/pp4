from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class blog_post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title