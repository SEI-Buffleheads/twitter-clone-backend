from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer, UserSerializer, CommentSerializer
from .models import Post, Comment
from authentication.models import User
from rest_framework import permissions, viewsets
from .permissions import IsOwner

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    def get_queryset(self):
        if self.request.user:
            return User.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = PostSerializer
    def get_queryset(self):
        if self.request.user:
            return Post.objects.all()
            
class CommentViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = CommentSerializer
    def get_queryset(self):
        if self.request.user:
            return Comment.objects.all()


class CommentListAPIView(ListCreateAPIView):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
  permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)

  def perform_create(self, serializer):
    return serializer.save(owner=self.request.user)
  def get_queryset(self):
    return self.queryset.filter(owner=self.request.user)

class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
  permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)
  lookup_field = "id"

  def perform_create(self, serializer):
    return serializer.save(owner=self.request.user)
  def get_queryset(self):
    return self.queryset.filter(owner=self.request.user)


class PostListAPIView(ListCreateAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)

  def perform_create(self, serializer):
    return serializer.save(owner=self.request.user)
  def get_queryset(self):
    return self.queryset.filter(owner=self.request.user)

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)
  lookup_field = "id"

  def perform_create(self, serializer):
    return serializer.save(owner=self.request.user)
  def get_queryset(self):
    return self.queryset.filter(owner=self.request.user)