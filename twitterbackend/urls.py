from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
    path('account/posts/',include('twitterapi.urls')),
    path('',include('twitterapi.userUrls'))
]
