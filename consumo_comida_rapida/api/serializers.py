from rest_framework import serializers
from consumo_comida_rapida.models import consumo_comida_rapida

class ConsumoComidaRapidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumo_comida_rapida
        fields = ['id', 'nombre']
        