from django.urls import path
from .views import UserListApiView

urlpatterns = [
  path('', UserListApiView.as_view(), name="user"),
  path('<int:id>', UserListApiView.as_view(), name="user"),
]