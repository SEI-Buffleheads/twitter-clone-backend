from django.urls import path
from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
  path('', PostListAPIView.as_view(), name="post"),
  path('<int:id>', PostDetailAPIView.as_view(), name="post")
]