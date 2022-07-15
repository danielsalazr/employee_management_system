from django.contrib import admin
from django.apps import AppConfig

# Register your models here.
class EmpleadoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'empleado'
