from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin

class User(models.Model):
  username = models.CharField(max_length=128)
  email = models.CharField(max_length=128)
  DOB= models.CharField(max_length=128)
  description = models.CharField(max_length=10000 , blank=True)
  followerList = models.ManyToManyField("self", blank=True)
  followingList = models.ManyToManyField("self", blank=True)
  ProfileIMG = models.CharField(max_length=128, blank=True)
  ProfileBackgroundIMG = models.CharField(max_length=128, blank=True)
  likedPosts = models.ManyToManyField('Post',related_name='likedTweets', blank=True)
  Tweets = models.ManyToManyField('Post',related_name='Tweets', blank=True)
  Comments = models.ManyToManyField('Post', related_name='post', blank=True)
  Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
  def __str__(self):
    return f'{self.username} - {self.id}'

class Post(models.Model):
  OwnerID = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE, null=True)
  Text = models.CharField(max_length=128)
  Likes = models.IntegerField(default=0,blank=True)
  LikedUsers = models.ManyToManyField('User',related_name='likedUsers', blank=True)
  URL = models.CharField(max_length=128, blank=True)
  ImageURL = models.CharField(max_length=128, blank=True)
  Comments = models.ManyToManyField('Comment',related_name='comment', blank=True)
  Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
  def __str__(self):
    return f'{self.OwnerID}'

class Comment(models.Model):
  PostID = models.ForeignKey(Post, related_name='postOwner', on_delete=models.CASCADE, null=True)
  OwnerID = models.ForeignKey(User, related_name='commentOwner', on_delete=models.CASCADE, null=True)
  Text = models.CharField(max_length=128)
  ImageURL = models.CharField(max_length=128, blank=True)
  Likes = models.IntegerField(default=0,blank=True)
  LikedUsers = models.ManyToManyField('User',related_name='likedCommentUsers', blank=True)
  Comments = models.ManyToManyField("self", blank=True)
  Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
  def __str__(self):
    return f'{self.id}'

