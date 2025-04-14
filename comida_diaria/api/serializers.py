from rest_framework import serializers
from comida_diaria.models import comida_diaria
class ComidaDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = comida_diaria
        fields = ['id', 'nombre']