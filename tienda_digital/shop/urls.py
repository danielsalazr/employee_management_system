from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "shop"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("lista", views.listado, name="lista"),
    path('listado', views.listTemplate,name='listado'),
    path('crearproducto', views.crearProducto ,name='crearproducto'),
    path('empleados/', views.ShopView.as_view() ,name='empleados'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)