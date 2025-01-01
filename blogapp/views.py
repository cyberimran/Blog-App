from django.shortcuts import render, redirect
from .models import BlogPost
from django.contrib.auth.models import User, auth
from django.contrib import messages

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

#Register Page
def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        username = request.POST.get('email')
        if confirmpassword==password:
            check_user = User.objects.filter(email=email)
            if check_user.exists():
                messages.add_message(request, messages.INFO, "Account already exists.")
                return redirect('/login/')
            user = User.objects.create_user(first_name=name, username=username, email=email, password=password)
            user.save()
            user = auth.authenticate(request, username=username, password=password)
            auth.login(request, user)
            return redirect("/")
        else:
            messages.add_message(request, messages.INFO, "Passwords do not match.")
    context={"page_title":"Register - CYBER IMRAN", "css_file":"css/register.css"}
    return render(request, 'register.html', context)

#Login Page
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
        else:
            messages.add_message(request, messages.INFO, "Invalid credentials.")
    context={"page_title":"Login - CYBER IMRAN", "css_file":"css/login.css"}
    return render(request, 'login.html', context)
