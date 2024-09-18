from django.shortcuts import render, redirect
from pago.models import Usuario
from django.utils import timezone

# Create your views here.

def landing(request):
  if request.method == 'POST':
    cedula = request.POST.get('cedula')
    usuario = Usuario.objects.get_or_create(cedula = cedula)
    return redirect(datosPago, cedula=cedula)

  return render(request, 'landing.html')

def sobre_nosotros(request):
  return render(request, 'sobre_nosotros.html')

def ia(request):
  return render(request, 'ia.html')

def datosPago(request, cedula):
  bandera = False
  usuario = Usuario.objects.get(cedula = cedula)
  if request.method == 'POST':
    saldo = request.POST.get('montoRecargar')
    usuario.saldo += float(saldo)
    usuario.fecha_registro = timezone.now()
    usuario.save()
    bandera = True


  return render(request, 'datosTarjeta.html', {'usuario':usuario, 'bandera': bandera})
