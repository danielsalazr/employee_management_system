from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import *



crearExperienciaProperties={
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

"""
    crearExperiancia
    Swagger Configuration
"""

request_bodyCrearExperiencia = openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    title = 'Body',
    properties={
        
        'n_documento': openapi.Schema(type=openapi.TYPE_STRING, description='string', default='11111111'),
        'anio': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer', default=2023),
        'mes': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer', default=12),
        'empresa': openapi.Schema(type=openapi.TYPE_STRING, description='string', default='enterprise_name'),
        'jefe_inmediato': openapi.Schema(type=openapi.TYPE_STRING, description='string', default='boss_name'),
        'cargo': openapi.Schema(type=openapi.TYPE_STRING, description='string', default='Job_position'),
        'responsabilidades': openapi.Schema(type=openapi.TYPE_STRING, description='string', default='Responsabilities description'),
        'logros': openapi.Schema(type=openapi.TYPE_STRING, description='string', default="Awards_description"), 
})

responsesCrearExperiencia={
        # 200: {"success":'OK'},
        200 : ExperienciaSerializer,
        500: 'Error',
}



"""
    getEmpleado
    Swagger Configuration
"""

empleadoResponses = {
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


"""
    EmpleadosView
    Swagger Configuration
"""


# Delete