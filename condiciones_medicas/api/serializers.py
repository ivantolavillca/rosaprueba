from rest_framework import serializers
from condiciones_medicas.models import condiciones_medicas

class CondicionesMedicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = condiciones_medicas
        fields = ['id', 'nombre']
