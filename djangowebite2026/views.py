
# from django.http import HttpResponse
# # pertemuan 2 URLS atau route basic tetapi nanti yang bagus garus di views.py buat file view.py di djangowebsite2026
# def index(request):
#     return HttpResponse("Hello, World!")

# def about(request):
#     return HttpResponse("This is the about page.")


#Django URL Configuration 
#pertemuan 3 untuk membuat template html yang lebih bagus daripada hanya menggunakan HttpResponse
# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# def about(request): 
#     return render(request, 'about.html')

