from django.shortcuts import render

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def entrada(request):
    return render(request,"AppCoder/entrada.html")

def nosotros(request):
    return render(request,"AppCoder/nosotros.html")

def cursos(request):
    return render(request,"AppCoder/cursos.html")

def contacto(request):
    return render(request,"AppCoder/contacto.html")