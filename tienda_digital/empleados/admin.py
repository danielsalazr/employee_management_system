from django.contrib import admin
from django.apps import AppConfig
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import (
    Empleados,
    Estudios,
    Experiencia_laboral,
    TipoDocumento,
    TipoSangre
)

from dataclasses import fields

# Register your models here.
@admin.register(Empleados)
class EmpleadoAdmin(admin.ModelAdmin):
    #default_auto_field = 'django.db.models.BigAutoField'
    #name = 'empleado'

    list_display = ('nombre','apellido','numero_documento','foto')

@admin.register(Estudios)
class EstudiosAdmin(admin.ModelAdmin):
    pass
    # list_display = ('num_documento','anio','mes','estudio','institucion', 'titulo_obtenido')


@admin.register(Experiencia_laboral)
class ExperienciaAdmin(admin.ModelAdmin):
    pass
    # list_display = ('n_documento','anio','mes','empresa')

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

@admin.register(TipoSangre)
class TipoSangreAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')