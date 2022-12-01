from django.db import models
from django.conf import settings

class Post(models.Model):
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post_owner", null=True)
  text = models.CharField(max_length=128, blank=False)
  title = models.CharField(max_length=1000, default="Text")
  date = models.DateTimeField(auto_now_add = True)
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_liked', blank=True)

class Comment(models.Model):
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_owner", null=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_its_on", null=True)
  text = models.CharField(max_length=128, blank=False)
  title = models.CharField(max_length=128, default="Text")
  date = models.DateTimeField(auto_now_add = True)
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_likes', blank=True)
