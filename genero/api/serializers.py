from rest_framework import serializers
from genero.models import genero

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = genero
        fields = ['id', 'nombre']
        