# Generated by Django 4.2.13 on 2024-05-24 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_post_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='favorites',
        ),
    ]