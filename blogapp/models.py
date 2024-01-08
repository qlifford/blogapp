from django.db import models
from django.contrib.auth.models import User

class RegUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="likes", null=True, blank=True, default='0')

    def __str__(self):
        return self.title
