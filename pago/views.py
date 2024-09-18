from django.shortcuts import render

# Create your views here.
def datosPago(request):
    return render(request, 'datosTarjeta.html')