from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.conf import settings
from datetime import datetime

# class User(models.Model):
#   username = models.CharField(max_length=128)
#   email = models.CharField(max_length=128)
#   DOB= models.CharField(max_length=128)
#   description = models.CharField(max_length=10000 , blank=True)
#   followerList = models.ManyToManyField("self", blank=True)
#   followingList = models.ManyToManyField("self", blank=True)
#   ProfileIMG = models.CharField(max_length=128, blank=True)
#   ProfileBackgroundIMG = models.CharField(max_length=128, blank=True)
#   likedPosts = models.ManyToManyField('Post',related_name='likedTweets', blank=True)
#   Tweets = models.ManyToManyField('Post',related_name='Tweets', blank=True)
#   Comments = models.ManyToManyField('Post', related_name='post', blank=True)
#   Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
#   def __str__(self):
#     return f'{self.username} - {self.id}'
class UserManager(BaseUserManager):
  def create_user(self, username, email, password=None):
    if username is None:
      raise TypeError("Please enter a username")
    if email is None:
      raise TypeError("Please enter an email")
    
    user = self.model(username = username, email = self.normalize_email(email))
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, username, email, password=None):
    if username is None:
      raise TypeError("Please enter a username")
    if email is None:
      raise TypeError("Please enter an email")
    user = self.create_user(username, email , password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return user

class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=128, unique = True, db_index= True)
  email = models.EmailField(max_length=128, unique = True, db_index= True)
  is_active = models.BooleanField(default = True)
  is_staff = models.BooleanField(default = False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  objects = UserManager()

  def __str__(self):
    return f'{self.email}'
  def tokens(self):
    return ''
    


class Post(models.Model):
  # author = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
  # OwnerID = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE, null=True)
  Text = models.CharField(max_length=128)
  # Likes = models.IntegerField(default=0,blank=True)
  # LikedUsers = models.ManyToManyField('User',related_name='likedUsers', blank=True)
  # URL = models.CharField(max_length=128, blank=True)
  # ImageURL = models.CharField(max_length=128, blank=True)
  # Comments = models.ManyToManyField('Comment',related_name='comment', blank=True)
  # Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
  def __str__(self):
    return f'{self.author}'



# class Comment(models.Model):
#   PostID = models.ForeignKey(Post, related_name='postOwner', on_delete=models.CASCADE, null=True)
#   OwnerID = models.ForeignKey(User, related_name='commentOwner', on_delete=models.CASCADE, null=True)
#   Text = models.CharField(max_length=128)
#   ImageURL = models.CharField(max_length=128, blank=True)
#   Likes = models.IntegerField(default=0,blank=True)
#   LikedUsers = models.ManyToManyField('User',related_name='likedCommentUsers', blank=True)
#   Comments = models.ManyToManyField("self", blank=True)
#   Date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
#   def __str__(self):
#     return f'{self.id}'

