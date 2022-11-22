from django.contrib import admin
from django.urls import path, include
from twittertestapi.views import UserViewSet, PostViewSet, CommentViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenVerifyView

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]

