from rest_framework import serializers
from clasificacion_peso.models import Clasificacion

class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = ['id', 'nombre']
        ref_name = 'ClasificacionPesoSerializer'  # Nombre único para este serializador