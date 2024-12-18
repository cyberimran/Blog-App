from django.shortcuts import render

def home(request):
    return render(request, 'home.html', context={"page_title":"BLOG APP USING DJANGO"})