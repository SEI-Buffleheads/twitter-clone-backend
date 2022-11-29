from django.contrib import admin
from .models import Post
from authentication.models import User

admin.site.register(Post)
admin.site.register(User)