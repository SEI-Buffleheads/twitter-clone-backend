from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.conf import settings
from datetime import datetime

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
    
