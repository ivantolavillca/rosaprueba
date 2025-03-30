from rest_framework import serializers
from personas.models import Personas, Clasificacion 
from clasificacion_peso.api.serializers import ClasificacionSerializer
from decimal import Decimal
from django.core.exceptions import ValidationError

from rest_framework import serializers
from personas.models import Clasificacion


class PersonaSerializer(serializers.ModelSerializer):
    clasificacion = ClasificacionSerializer(read_only=True)

    class Meta:
        model = Personas
        fields = ['id', 'nombre_completo', 'genero','edad', 'peso', 'estatura', 'clasificacion', 'imc']

    def validate_edad(self, value):
        if value < 13 or value > 18:
            raise ValidationError("La edad debe estar entre 13 y 18 años.")
        return value

    def validate_peso(self, value):
        if not isinstance(value, Decimal):
            raise ValidationError("El peso debe ser un número decimal.")
        if value <= 0:
            raise ValidationError("El peso debe ser un valor positivo.")
        return value

    def validate_estatura(self, value):
        if not isinstance(value, Decimal):
            raise ValidationError("La estatura debe ser un número decimal.")
        if value <= 0:
            raise ValidationError("La estatura debe ser un valor positivo.")
        return value

class ReportPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['nombre_completo','genero', 'edad', 'peso', 'estatura', 'clasificacion', 'imc']
        
class ModeloDatos(serializers.Serializer):
    edad = serializers.FloatField()
    peso = serializers.FloatField()
    estatura = serializers.FloatField()
    genero = serializers.FloatField()