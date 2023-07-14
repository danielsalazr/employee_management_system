from ast import Delete
from django.shortcuts import render
from  .models import *
from django.http import HttpResponse, JsonResponse
from urllib import request, response
from .serializers import EmpleadosSerializer, EstudiosSerializer, ExperienciaSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from django.views import generic

from django.conf import settings
    
    
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "empleados/principal.html"

#Vista del listado completo de empleados
class ListV(generic.ListView):
    template_name= "empleados/verEmpleados.html"
    context_object_name = "empleados"

    def get_queryset(self):
        """return de last five published questions"""
        #traerlas desde las mas recientes hasta las mas antiguas con el -pub_date
        return Empleados.objects.order_by("nombre")#[:5]



def crearEmpleado(request):
    return render(request, 'empleados/crearEmpleado.html')

def actualizarEmpleado(request):
    return render(request, 'empleados/actualizarEmpleado.html')

def eliminarEmpleado(request):
    return render(request, 'empleados/eliminarEmpleado.html')

def consultarEmpleado(request):
    return render(request, 'empleados/consultarEmpleado.html')

def devolverConsulta(request):
    print (request.data)

def consultarUno(request):
    if 'busqueda' in request.GET:
        #print(request.GET['parametro'])
        busqueda= request.GET['busqueda']
        documento = busqueda

            
        #busqueda = Empleados.objects.filter(numero_documento__contains=documento)
        busqueda = Empleados.objects.get(numero_documento__contains=documento)
        estudios = Estudios.objects.filter(num_documento=documento)
        experiencia = Experiencia_laboral.objects.filter(n_documento=documento)
        # print(busqueda.nombre)
        #busqueda.foto = settings.MEDIA_ROOT / str(busqueda.foto)
        return render(
            request, 'empleados/verUnEmpleado.html', 
            {
                'empleados': busqueda,
                'estudios': estudios,
                'experiencia':experiencia
            }
        )

    return response("Error")
    #print(busqueda)
    return render(request, 'empleados/verUnEmpleado.html', {'empleados': busqueda})


class EmpleadosView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    # swagger_schema = None
    

    # @swagger_auto_schema(methods=['put', 'post'], request_body=EmpleadosSerializer)
    @swagger_auto_schema(responses=
        {
            200: EmpleadosSerializer(many=True),
            400: 'There\'s no selection',
        }
    )
    def get(self, request, id=0):# *args, **kwargs):
        """
        Obtener informacionde  empleados

        Retorna los datos de todos los empleados de la plataforma
        """
        print(id)
        print(args)
        print(id)
        ccId = request.GET.get('numero_documento')
        print(ccId)

        if ccId :
            try:
                personal = Empleados.objects.filter(Q(numero_documento=str(ccId)))#.order_by('-id')[:limit]
                serializer = EmpleadosSerializer(personal, many =True)

                return Response(serializer.data[0], status=status.HTTP_200_OK)
            except: 
                
                return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)


        else:
            personal = Empleados.objects.all()
            serializer = EmpleadosSerializer(personal, many =True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    

    # @swagger_auto_schema(operation_description="description")
    @swagger_auto_schema(
        # request_body=openapi.Schema(
        # type=openapi.TYPE_OBJECT,
        # properties={
        #     'phone': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
        #     'body': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
        # }),
        # method=['post'],
        request_body=EmpleadosSerializer(many=True),
        
        responses=
        {
            200: EmpleadosSerializer(many=True),
            400: 'There\'s no selection',
        },
        # manual_parameters=[
        #     openapi.Parameter('file', openapi.IN_FORM, type=openapi.TYPE_FILE, description='Document to be uploaded'),
        #     openapi.Parameter('s3_key', openapi.IN_FORM, type=openapi.TYPE_STRING, description='S3 Key of the Document '
        #                                                                                        '(folders along with name)')
        # ],
        
    )
    def post(self, request,*args, **kwargs):
        #print(request.data)
        """
        Crear un empleado

        Si la consulta se realiza con exito se crea un empleado
        """
        empleados_serializer = EmpleadosSerializer(data=request.data)
        if empleados_serializer.is_valid():
            empleado = empleados_serializer.save()

        return Response(EmpleadosSerializer(empleado).data)


    #por cuestiones de tiempo la actualizacion y elminacion formulario lo realizo sin verificacion
    def delete(self, request,*args, **kwargs):
        #print(request.data["nombre"])
        empleado = Empleados.objects.get(nombre=request.data["nombre"], numero_documento=request.data["numero_documento"])
        if empleado:
            empleado.delete()

        return Response("Eliminado")

    def put(self, request,*args, **kwargs):
        # print(request.data)
        # print(request.data["numero_documento"])
        Empleados.objects.filter(numero_documento=request.data["numero_documento"]).update( nombre=request.data["nombre"], apellido=request.data["apellido"], tipo_documento = request.data["tipo_documento"], correo = request.data["correo"], telefono= request.data["telefono"], tipo_sangre= request.data["tipo_sangre"], foto= request.data['foto'])

        return Response("Actualizado")


# @swagger_auto_schema(
#         # methods=['post'],
#         # request_body=openapi.Schema(
#         # type=openapi.TYPE_OBJECT,
#         # properties={
#         #     'phone': openapi.Schema(type=openapi.TYPE_STRING, description='lol'),
#         #     'body': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
#         # },
#         # schema=EmpleadosSerializer(many=True),
        
#         # override = {
#         #     200: 'res',
#         # }
        
#         # ),

        

        
#         # request_body=EmpleadosSerializer,
        
#         # responses=
#         # {
#         #     200: EmpleadosSerializer(many=True),
#         #     400: 'There\'s no selection',
#         # },
#         manual_parameters=[
#             openapi.Parameter('file', openapi.IN_FORM, type=openapi.TYPE_FILE, description='Document to be uploaded'),
#             openapi.Parameter('s3_key', openapi.IN_FORM, type=openapi.TYPE_STRING, description='S3 Key of the Document '
#                                                                                                '(folders along with name)')
#         ],
        
#     )

@swagger_auto_schema(
    methods=['POST'],
    # operation_summary="Sum of Two numbers",
    request_body = EmpleadosSerializer,
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            title="susue",
            description ='bacas bacas',
            properties={
              'phone': openapi.Schema(type=openapi.TYPE_STRING, description='lol'),
              'body': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
            }
        ),

        '500': 'Error',

    }
)
@api_view(['POST'])
def getEmpleado(request):
    """
    post de post

    se hace el post

    """
    experiencia_serializer = ExperienciaSerializer(data=request.data)
    if experiencia_serializer.is_valid():
        # print("True")
        experiencia = experiencia_serializer.save()

    return Response(ExperienciaSerializer(experiencia).data)

class ExperienceView(generic.TemplateView):
    template_name = "empleados/ingresarExperiencia.html"

@api_view(['POST'])
def crearExperiencia(request):
    experiencia_serializer = ExperienciaSerializer(data=request.data)
    if experiencia_serializer.is_valid():
        # print("True")
        experiencia = experiencia_serializer.save()

    return Response(ExperienciaSerializer(experiencia).data)



class StudiesView(generic.TemplateView):
    template_name = "empleados/ingresarEstudios.html"

@api_view(['POST'])
def crearEstudios(request):
    estudios_serializer = EstudiosSerializer(data=request.data)
    # print(request.data)
    # print(request.data['num_documento'])
    if estudios_serializer.is_valid():
        # print("True")
        #q= Estudios.objects
        #q.create(num_documento=Empleados.objects.get(numero_documento=), anio=2015, mes=10, estudio="Gramatica",institucion="USC",titulo_obtenido="master en gramatica")
        estudios= estudios_serializer.save()

    return Response(EstudiosSerializer(estudios).data)