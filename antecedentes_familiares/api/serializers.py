from rest_framework import serializers
from antecedentes_familiares.models import antecedentes_familiares 
class AntecedentesFamiliaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = antecedentes_familiares
        fields = ['id', 'nombre']
        