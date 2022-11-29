from django.urls import path
from .views import CommentListAPIView, CommentDetailAPIView
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()

urlpatterns = [
  path('', CommentListAPIView.as_view(), name="comments"),
  path('<int:id>', CommentDetailAPIView.as_view(), name="commentsbyID"),
]