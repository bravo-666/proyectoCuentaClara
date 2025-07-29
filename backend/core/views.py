from django.shortcuts import render

def bienvenido(request):
    return render(request, 'bienvenido.html')

def login_view(request):
    return render(request, 'inicioSesion.html')  

def nuevo_usuario(request):
    return render(request, 'nuevo_usuario.html')
