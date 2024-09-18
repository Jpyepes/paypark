from django.db import models

# Create your models here.

class Usuario(models.Model):
    cedula = models.CharField(max_length=15)
    saldo = models.FloatField(default=0)
    fecha_registro = models.DateTimeField(null=True)
