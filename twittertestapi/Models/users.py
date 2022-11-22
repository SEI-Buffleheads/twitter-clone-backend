from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

from .comments import Comment

class User(models.Model):
  username = models.CharField(max_length=128)
  email = models.CharField(max_length=128)
  DOB= models.CharField(max_length=128)
  description = models.CharField(max_length=10000 , blank=True)
  followingCount = models.IntegerField(default=0,blank=True)
  followerCount = models.IntegerField(default=0,blank=True)
  followerList = models.ManyToManyField("self", blank=True)
  followingList = models.ManyToManyField("self", blank=True)
  ProfileIMG = models.CharField(max_length=128, blank=True)
  ProfileBackgroundIMG = models.CharField(max_length=128, blank=True)
  isUser = models.BooleanField(blank=True, null=True)
  followingStatus = models.BooleanField(blank=True, null=True)
  followRequestSent = models.BooleanField(blank=True, null=True)
  # likedPosts = models.ManyToManyField(Post, blank=True)
  # Tweets = models.ManyToManyField(Post, blank=True)
  # Comments = models.ManyToManyField(Post, blank=True)
  Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)