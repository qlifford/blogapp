# Generated by Django 5.0.1 on 2024-01-08 11:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0013_remove_blog_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reguser',
            name='cpassword',
        ),
        migrations.RemoveField(
            model_name='reguser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reguser',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(blank=True, default='0', null=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
