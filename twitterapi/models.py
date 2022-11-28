from django.db import models
from authentication.models import User

class Post(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  text = models.CharField(max_length=128)
  date = models.DateTimeField(auto_now_add = True)
