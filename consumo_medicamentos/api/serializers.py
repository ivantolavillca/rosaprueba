from rest_framework import serializers
from consumo_medicamentos.models import consumo_medicamentos

class ConsumoMedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumo_medicamentos
        fields = ['id', 'nombre']
        