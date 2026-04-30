from django.apps import AppConfig
#tempat untuk mengatur konfigurasi aplikasi kita, seperti nama aplikasi, label, dan lain-lain. AppConfig adalah sebuah kelas yang digunakan untuk mengkonfigurasi aplikasi Django. 
# Kelas ini biasanya didefinisikan dalam file apps.py di dalam direktori aplikasi kita.

class blogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
