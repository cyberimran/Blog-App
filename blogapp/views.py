from django.shortcuts import render
from .models import BlogPost

def home(request):
    blogs = BlogPost.objects.order_by('-dateandtime')[:4]
    for blog in blogs:
        print(blog.dateandtime.date())
        context={"page_title":"BLOG APP USING DJANGO", "blogs":blogs}
    return render(request, 'home.html', context)

def blogspage(request):
    query = request.GET.get('q')
    if query:
        blogs = BlogPost.objects.filter(title__icontains=query)
        context={"page_title":"ALL BLOGS", "blogs":blogs, "searched":query}
        return render(request, 'blogs.html', context)
    blogs = BlogPost.objects.order_by('-dateandtime')
    context={"page_title":"ALL BLOGS", "blogs":blogs, "searched":query}
    return render(request, 'blogs.html', context)

def blog(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    print(blog.category)
    context={"page_title":blog.title, "blog":blog}
    return render(request, 'blog.html', context)