from  rest_framework import serializers
from .models import Empleados, Estudios, Experiencia_laboral

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = [
            'numero_documento',
            'nombre',
            'apellido',
            'tipo_documento',
            'correo',
            'telefono',
            'tipo_sangre',
            'foto',
        ]

        def to_representation(self, instance):
            valor_actual = instance.campo_a_reemplazar

class DeleteEmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = [
            'numero_documento',
            'nombre',
        ]

class EstudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudios
        fields = '__all__'



class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencia_laboral
        # fields = '__all__'
        fields = [
            'n_documento',
            'fecha_inicio',
            'fecha_final',
            'empresa',
            'jefe_inmediato',
            'cargo',
            'responsabilidades',
            'logros',
        ]