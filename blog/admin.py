from django.contrib import admin
from .models import Post
from .models import Rating

admin.site.register(Post)
admin.site.register(Rating)