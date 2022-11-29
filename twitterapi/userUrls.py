from django.urls import path
from .views import UserViewSet, PostViewSet
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='allPost')

urlpatterns = [
  path('', include(router.urls))
  
]