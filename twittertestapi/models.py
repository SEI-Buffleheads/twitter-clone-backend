from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=128)
  email = models.CharField(max_length=128)
  DOB= models.CharField(max_length=128)
  description = models.CharField(max_length=10000 , blank=True)
  followingCount = models.IntegerField(default=0,blank=True)
  followerCount = models.IntegerField(default=0,blank=True)
  followerList = ArrayField(models.CharField(max_length=10000),blank=True, null=True)
  followingList = ArrayField(models.CharField(max_length=10000), blank=True, null=True)
  ProfileIMG = models.CharField(max_length=128, blank=True)
  ProfileBackgroundIMG = models.CharField(max_length=128, blank=True)
  isUser = models.BooleanField(blank=True, null=True)
  followingStatus = models.BooleanField(blank=True, null=True)
  followRequestSent = models.BooleanField(blank=True, null=True)
  likedPosts = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  Tweets = ArrayField(models.CharField(max_length=200),blank=True, null=True)
  Comments = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
  def __str__(self):
    return f'{self.username} - {self.email} - {self.DOB} - {self.description} - {self.followingCount} - {self.followerCount} - {self.followerList}- {self.followingList}- {self.ProfileIMG}- {self.ProfileBackgroundIMG}- {self.isUser}- {self.followingStatus}- {self.followRequestSent}- {self.likedPosts}- {self.Tweets} - {self.Comments}'

class Post(models.Model):
  OwnerID = models.CharField(max_length=128)
  Text = models.CharField(max_length=128)
  Likes = models.IntegerField(default=0,blank=True)
  LikedUsers = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  URL = models.CharField(max_length=128, blank=True)
  ImageURL = models.CharField(max_length=128, blank=True)
  Comments = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
  def __str__(self):
    return f'{self.OwnerID} - {self.Text}- {self.Likes}- {self.LikedUsers}- {self.URL}- {self.ImageURL}- {self.Comments}'

class Comment(models.Model):
  PostID = models.CharField(max_length=128)
  OwnerID = models.CharField(max_length=128)
  Text = models.CharField(max_length=128)
  ImageURL = models.CharField(max_length=128, blank=True)
  Likes = models.IntegerField(default=0,blank=True)
  LikedUsers = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  Replies = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
  def __str__(self):
    return f'{self.name} - {self.subject}'