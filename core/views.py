from django.shortcuts import render,HttpResponse

# Create your views here.
def index(requets):
    return HttpResponse("<h1>Home</h1>")

def about(request):
    return HttpResponse("<h1>Nosotros</h1>")

def services(request):
    return HttpResponse("<h1>Servicios</h1>")

def store(request):
    return HttpResponse("<h1>nuestra Tienda</h1>")

def conctac(request):
    return HttpResponse("<h1>Contacto</h1>")

def blog(request):
    return HttpResponse("<h1>Visita nnuestro Blog informativo</h1>")

def samples(request):
    return HttpResponse("<h1>Pruebas</h1>")    