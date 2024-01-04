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
        fields = '__all__'
        # fields = [
        #     'n_documento',
        #     'fecha_inicio',
        #     'fecha_final',
        #     'empresa',
        #     'jefe_inmediato',
        #     'cargo',
        #     'responsabilidades',
        #     'logros',
        # ]

    # def create(self, validated_data):
    #     console.log(validated_data)
    #     return user

    # def validate_n_documento(self, value):
    #     # try:
    #         # Attempt to retrieve the object from the database
    #     obj = Empleados.objects.get(numero_documento=value)
    #     print(self)
    #     # self.context['validated_data']['n_documento'] = obj
    #     # except ObjectDoesNotExist:
    #     #     # If the object does not exist, raise a validation error
    #     #     raise serializers.ValidationError(f"Object with n_documento {value} does not exist.")

    #     # Return the original value if the object exists
    #     return obj