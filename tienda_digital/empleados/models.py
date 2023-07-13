from pyexpat import model
from django.db import models

# Create your models here.
class Empleados (models.Model):
    numero_documento = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_documento = models.CharField(max_length=20)
    correo = models.CharField(max_length=70)
    telefono = models.CharField(max_length=50)
    tipo_sangre = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='empleados/photo')


class Estudios(models.Model):
    num_documento = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    anio = models.IntegerField(default=2000)
    # anioInicio = models.IntegerField(default=0)
    # anioIFinal = models.IntegerField(default=0)
    mes = models.IntegerField(default=1)
    estudio =models.CharField(max_length=70)
    institucion = models.CharField(max_length=50)
    titulo_obtenido = models.CharField(max_length=50)


class Experiencia_laboral(models.Model):
    n_documento = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    anio = models.IntegerField(default=2000)
    mes = models.IntegerField(default=1)
    empresa = models.CharField(max_length= 70)
    jefe_inmediato = models.CharField(max_length=50)
    cargo = models.CharField(max_length=30)
    responsabilidades = models.TextField((""))
    logros= models.TextField((""))