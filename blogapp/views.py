from django.shortcuts import render
from .models import BlogPost

def home(request):
    blogs = BlogPost.objects.order_by('-dateandtime')[:4]
    context={"page_title":"BLOG APP USING DJANGO", "blogs":blogs}
    return render(request, 'home.html', context)