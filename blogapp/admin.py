from django.contrib import admin
from .models import Category, BlogPost, Image

admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Image)