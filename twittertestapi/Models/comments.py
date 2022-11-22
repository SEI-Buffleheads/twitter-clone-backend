from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

from .posts import Post

class Comment(models.Model):
  PostID = models.ForeignKey("Post", related_name='comment', on_delete=models.CASCADE, null=True)
  OwnerID = models.ForeignKey("User", related_name='comment', on_delete=models.CASCADE, null=True)
  Text = models.CharField(max_length=128)
  ImageURL = models.CharField(max_length=128, blank=True)
  Likes = models.IntegerField(default=0,blank=True)
  LikedUsers = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  Replies = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
  def __str__(self):
    return f'{self.PostID} - {self.OwnerID}'