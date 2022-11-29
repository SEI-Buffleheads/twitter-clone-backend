from rest_framework import serializers
from .models import Post
from authentication.models import User

class PostSerializer(serializers.ModelSerializer):
  owner = serializers.CharField(max_length=255, min_length = 3, read_only= True)
  class Meta:
    model = Post
    fields = [ "text", "date", "title",'owner','id']
  
class UserSerializer(serializers.ModelSerializer):
  Post = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
  class Meta:
    model = User
    fields = ['username','Post', 'created_at','id']