from rest_framework import serializers
from actividades_fisicas.api.serializers import ActividadesFisicasSerializer
from antecedentes_familiares.api.serializers import AntecedentesFamiliaresSerializer
from comida_diaria.api.serializers import ComidaDiariaSerializer
from condiciones_medicas.api.serializers import CondicionesMedicasSerializer
from consumo_comida_rapida.api.serializers import ConsumoComidaRapidaSerializer
from consumo_medicamentos.api.serializers import ConsumoMedicamentosSerializer
from estres_ansiedad.api.serializers import EstresAnsiedadSerializer
from genero.api.serializers import GeneroSerializer
from personas.models import Personas, Clasificacion 
from consumo_comida_rapida.models import consumo_comida_rapida 
from comida_diaria.models import comida_diaria 
from actividades_fisicas.models import ActividadesFisicas 
from estres_ansiedad.models import estres_ansiedad 
from consumo_medicamentos.models import consumo_medicamentos 
from antecedentes_familiares.models import antecedentes_familiares 
from condiciones_medicas.models import condiciones_medicas 
from clasificacion_peso.api.serializers import ClasificacionSerializer
from decimal import Decimal
from django.core.exceptions import ValidationError

from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    clasificacion = ClasificacionSerializer(read_only=True)
    antecedentes_familiares = AntecedentesFamiliaresSerializer(read_only=True)
    condiciones_medicas = CondicionesMedicasSerializer(read_only=True)
    consumo_medicamentos = ConsumoMedicamentosSerializer(read_only=True)
    estres_ansiedad = EstresAnsiedadSerializer(read_only=True)
    actividades_fisicas = ActividadesFisicasSerializer(read_only=True)
    comida_diaria = ComidaDiariaSerializer(read_only=True)
    consumo_comida_rapida = ConsumoComidaRapidaSerializer(read_only=True)
    genero = GeneroSerializer(read_only=True)
    class Meta:
        model = Personas

        fields = ['id', 'nombre_completo', 'genero','edad', 'peso', 'estatura','antecedentes_familiares','condiciones_medicas','consumo_medicamentos','estres_ansiedad','actividades_fisicas','comida_diaria','consumo_comida_rapida', 'clasificacion', 'imc']

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
        fields = ['nombre_completo', 'genero','edad', 'peso', 'estatura','antecedentes_familiares','condiciones_medicas','consumo_medicamentos','estres_ansiedad','actividades_fisicas','comida_diaria','consumo_comida_rapida', 'clasificacion', 'imc']
        
class ModeloDatos(serializers.Serializer):
    edad = serializers.FloatField()
    peso = serializers.FloatField()
    estatura = serializers.FloatField()
    genero = serializers.FloatField()
    antecedentes_familiares = serializers.FloatField()
    condiciones_medicas = serializers.FloatField()
    consumo_medicamentos = serializers.FloatField()
    estres_ansiedad = serializers.FloatField()
    actividades_fisicas = serializers.FloatField()
    consumo_comida_rapida = serializers.FloatField()
    comida_diaria = serializers.FloatField()