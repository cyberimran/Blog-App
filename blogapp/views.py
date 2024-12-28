from django.shortcuts import render
from .models import BlogPost

#Home Page
def home(request):
    blogs = BlogPost.objects.order_by('-dateandtime')[:4]
    for blog in blogs:
        print(blog.dateandtime.date())
        context={"page_title":"BLOG APP USING DJANGO", "blogs":blogs, "css_file":"css/style.css"}
    return render(request, 'home.html', context)

#All Blogs Page
def blogspage(request):
    query = request.GET.get('q')
    if query:
        blogs = BlogPost.objects.filter(title__icontains=query)
        context={"page_title":"ALL BLOGS", "blogs":blogs, "searched":query, "css_file":"css/blogs.css"}
        return render(request, 'blogs.html', context)
    blogs = BlogPost.objects.order_by('-dateandtime')
    context={"page_title":"ALL BLOGS", "blogs":blogs, "searched":query, "css_file":"css/blogs.css"}
    return render(request, 'blogs.html', context)

#Blog Page
def blog(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    context={"page_title":blog.title, "blog":blog, "css_file":"css/blog.css"}
    return render(request, 'blog.html', context)

#About Page
def about(request):
    context={"page_title":"About - CYBER IMRAN", "css_file":"css/about.css"}
    return render(request, 'about.html', context)

#Contact Page
def contact(request):
    context={"page_title":"Contact - CYBER IMRAN", "css_file":"css/contact.css"}
    return render(request, 'contact.html', context)
    