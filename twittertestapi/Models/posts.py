from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.contrib.auth.models import User

from .users import User
from .comments import Comment

class Post(models.Model):
  OwnerID = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE, null=True)
  Text = models.CharField(max_length=128)
  Likes = models.IntegerField(default=0,blank=True)
  LikedUsers = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  URL = models.CharField(max_length=128, blank=True)
  ImageURL = models.CharField(max_length=128, blank=True)
  Comments = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
  def __str__(self):
    return f'{self.OwnerID}'

  def __str__(self):
    return f'{self.username}'