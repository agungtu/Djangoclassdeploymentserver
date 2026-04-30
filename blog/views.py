from django.shortcuts import render
#tempat untuk membuat fungsi atau kelas yang akan menangani permintaan dari user dan mengembalikan respon yang sesuai. 
# Views adalah sebuah fungsi atau kelas yang digunakan untuk menangani permintaan dari user dan mengembalikan respon yang sesuai. Views biasanya didefinisikan dalam file views.py di dalam direktori aplikasi kita.
# Create your views here.
#seperti controller 

def blogs(request):
    return render(request, 'blog.html')
