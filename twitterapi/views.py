from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer, UserSerializer
from .models import Post
from authentication.models import User
from rest_framework import permissions
from .permissions import IsOwner

class PostListAPIView(ListCreateAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permissions_classes = (permissions.IsAuthenticated)

  def perform_create(self, serializer):
    return serializer.save(owner=self.request.user)
  def get_queryset(self):
    return self.queryset.filter(owner=self.request.user)

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permissions_classes = (permissions.IsAuthenticated, IsOwner)
  lookup_field = "id"

  def perform_create(self, serializer):
    return serializer.save(owner=self.request.user)
  def get_queryset(self):
    return self.queryset.filter(owner=self.request.user)
  
class UserListApiView(ListCreateAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  permissions_classes = (permissions.IsAuthenticated)
  def perform_create(self, serializer):
    return serializer.save(owner=self.request.user)
  def get_queryset(self):
    return self.queryset.filter(owner=self.request.user)
