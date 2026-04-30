#Django URL Configuration 
#pintu masuk user untuk mengakses aplikasi web kita
#untuk mengatur URL yang akan diakses oleh user
from django.contrib import admin
from django.urls import path

# from .views import index, about # import views yang sudah dibuat di views.py atau memanggil fungsi index dan about yang sudah dibuat di views.py
from . import views # import views yang sudah dibuat di views.py atau memanggil fungsi index dan about yang sudah dibuat di views.py            
from blog import views as blog # import views yang sudah dibuat di views.py atau memanggil fungsi index dan about yang sudah dibuat di views.py
from kontak import views as kontak # import views yang sudah dibuat di views.py atau memanggil fungsi index dan about yang sudah dibuat di views.py
from biodata import views as biodata # import views yang sudah dibuat di views.py atau memanggil fungsi index dan about yang sudah dibuat di views.py   
from django.http import HttpResponse

# pertemuan 2 URLS atau route basic tetapi nanti yang bagus harus di views.py buat file view.py di djangowebsite2026
# def index(request):
#     return HttpResponse("Hello, World!")

# def about(request):
    # return HttpResponse("<h1>This is the about page.</h1>")

urlpatterns = [
    # path('', index, name='index'),
    # path('about/', about, name='about'),
    path('', views.index), # memanggil fungsi index yang sudah dibuat di views.py),
    path ('blog/', blog.blogs), # memanggil fungsi about yang sudah dibuat di views.py),
    path ('kontak/', kontak.kontaks), # memanggil fungsi about yang sudah dibuat di views.py),
    path('biodata/', biodata.bio), # memanggil fungsi biodata yang sudah dibuat di views.py),
    # path('admin/', admin.site.urls),
]
