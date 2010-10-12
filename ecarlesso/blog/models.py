from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length = 200)
    slug = models.SlugField()
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()

    author = models.CharField(max_length = 50)
    
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
