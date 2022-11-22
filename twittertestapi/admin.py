# Register your models here.
from django.contrib import admin
from .Models.models import User, Post, Comment
# from .Models.Test import Test, Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)