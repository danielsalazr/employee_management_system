from pyexpat import model
from django.db import models
from django.db.models import DO_NOTHING

# Create your models here.

class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)

class TipoSangre(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=3)

class Empleados (models.Model):
    id = models.AutoField(primary_key=True)
    numero_documento = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50,)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.DO_NOTHING, default=None, null=True, blank=True)
    correo = models.CharField(max_length=70, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    tipo_sangre = models.ForeignKey(TipoSangre, on_delete=models.DO_NOTHING, default=None, null=True, blank=True)
    foto = models.ImageField(upload_to='empleados/photo', null=True, blank=True)


class Estudios(models.Model):
    id = models.AutoField(primary_key=True)
    num_documento = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now=False,  default=None, null=True, blank=True)
    fecha_final = models.DateField(auto_now=False,  default=None, null=True, blank=True)
    # mes = models.IntegerField(default=1)
    estudio =models.CharField(max_length=70)
    institucion = models.CharField(max_length=50)
    titulo_obtenido = models.CharField(max_length=50)


class Experiencia_laboral(models.Model):
    id = models.AutoField(primary_key=True)
    n_documento = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now=False,  default=None, null=True, blank=True)
    fecha_final = models.DateField(auto_now=False,  default=None, null=True, blank=True)
    empresa = models.CharField(max_length= 70)
    jefe_inmediato = models.CharField(max_length=50)
    cargo = models.CharField(max_length=30)
    responsabilidades = models.TextField(max_length=200)
    logros = models.TextField(max_length=200)