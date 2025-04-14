from rest_framework import serializers
from actividades_fisicas.models import ActividadesFisicas 
class ActividadesFisicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadesFisicas
        fields = ['id', 'nombre']
        