from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "empleados"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("crearempleados/", views.crearEmpleado, name="crearempleado"),
    path('creacion/', views.EmpleadosView.as_view() ,name='creacion'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)