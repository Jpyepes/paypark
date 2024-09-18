from django.shortcuts import render

# Create your views here.

def landing(request):
  return render(request, 'landing.html')

def sobre_nosotros(request):
  return render(request, 'sobre_nosotros.html')

def datosPago(request):
    return render(request, 'datosTarjeta.html')
