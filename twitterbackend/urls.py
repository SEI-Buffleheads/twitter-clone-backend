from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
    path('user/posts/',include('twitterapi.urls')),
    path('user/comments',include('twitterapi.commentUrls')),
    path('',include('twitterapi.userUrls'))
]
