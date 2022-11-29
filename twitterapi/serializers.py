from rest_framework import serializers
from .models import Post, Comment
from authentication.models import User

class PostSerializer(serializers.ModelSerializer):
  owner = serializers.CharField(max_length=255, min_length = 3, read_only= True)
  class Meta:
    model = Post
    fields = [ "text", "date", "title",'owner','id']
  
class UserSerializer(serializers.ModelSerializer):
  # posts = serializers.PrimaryKeyRelatedField(PostSerializer,many=True)
  class Meta:
    model = User
    fields = ['username', 'created_at','id',]

class CommentSerializer(serializers.ModelSerializer):
  owner = serializers.CharField(max_length=255, min_length = 3, read_only= True)
  post = serializers.CharField(max_length=255, min_length = 3, read_only= True)
  class Meta:
    model = Comment
    fields = [ "text", "date", "title",'owner','id',"post"]