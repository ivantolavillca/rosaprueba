from rest_framework import serializers
from estres_ansiedad.models import estres_ansiedad

class EstresAnsiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = estres_ansiedad
        fields = ['id', 'nombre']
        