from django.urls import path
from .views import UserViewSet, PostViewSet, CommentViewSet
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'allposts', PostViewSet, basename='allPosts')
router.register(r'allcomments', CommentViewSet, basename='allComments')

urlpatterns = [
  path('', include(router.urls))
]