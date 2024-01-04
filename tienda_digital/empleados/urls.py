from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'employeexperience', views.EmployeeExperience)


app_name = "empleados"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("listaempleado/", views.ListV.as_view(), name="listaempleado"),

    path("crearempleado/", views.crearEmpleado, name="crearempleado"),

    path('empleados/', views.EmpleadosView.as_view() ,name='creacion'),
    # path('empleados/<int:id>/', views.EmpleadosView.as_view() ,name='empleadoById'),
    path('empleados/<int:id_number>/', views.getEmpleado ,name='empleadoById'),

    

    path('eliminarempleado/', views.eliminarEmpleado ,name='eliminacion'),
    path('actualizarempleado/', views.actualizarEmpleado,name='actualizacion'),

    path('consultarempleado/', views.consultarEmpleado ,name='consultar'),
    path('consultarUno/', views.consultarUno , name='consultarUno'),
    path('consultar/', views.devolverConsulta ,name='retornoconsulta'),

    path('experiencia/', views.ExperienceView.as_view() ,name='experiencia'),
    path('empleados/experience/<int:id_number>', views.EmployeeExperience.as_view() ,name='employee_experience'),

    # path('lulito/', views.Lulito.as_view() ,name='experiencia'),

    # path('', include(router.urls)),

    path('estudios/', views.StudiesView.as_view() ,name='estudios'),
    path('crearestudios/', views.crearEstudios ,name='crearestudios'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)