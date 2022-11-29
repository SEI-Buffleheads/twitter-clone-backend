from django.db import models
from django.conf import settings

class Post(models.Model):
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post_owner", null=True)
  text = models.CharField(max_length=128, blank=False)
  title = models.CharField(max_length=128, default="Text")
  date = models.DateTimeField(auto_now_add = True)
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_liked', blank=True)
