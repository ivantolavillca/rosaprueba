from django.db import models
from clasificacion_peso.models import Clasificacion
from antecedentes_familiares.models import antecedentes_familiares
from condiciones_medicas.models import condiciones_medicas
from consumo_medicamentos.models import consumo_medicamentos
from estres_ansiedad.models import estres_ansiedad
from actividades_fisicas.models import ActividadesFisicas
from comida_diaria.models import comida_diaria
from genero.models import genero
from consumo_comida_rapida.models import consumo_comida_rapida
from django.db.models import CASCADE
from django.core.exceptions import ValidationError
class Personas(models.Model):
    nombre_completo = models.CharField(max_length=255, verbose_name="Nombre completo")
    edad = models.IntegerField( verbose_name="Edad")
    peso = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso")
    estatura = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Estatura")
    imc = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="IMC", null=True, blank=True)  
    genero = models.ForeignKey(genero, on_delete=models.CASCADE,default=1, verbose_name="Género")  
    antecedentes_familiares = models.ForeignKey(antecedentes_familiares, on_delete=models.CASCADE,default=1, verbose_name="Antecedentes familiares")
    condiciones_medicas = models.ForeignKey(condiciones_medicas, on_delete=models.CASCADE,default=1, verbose_name="Condiciones médicas")
    consumo_medicamentos = models.ForeignKey(consumo_medicamentos, on_delete=models.CASCADE,default=1,verbose_name="Consumo de medicamentos")
    estres_ansiedad = models.ForeignKey(estres_ansiedad, on_delete=models.CASCADE,default=1, verbose_name="Estrés y ansiedad")
    actividades_fisicas = models.ForeignKey(ActividadesFisicas, on_delete=models.CASCADE,default=1, verbose_name="Actividades físicas")
    comida_diaria = models.ForeignKey(comida_diaria, on_delete=models.CASCADE,default=1, verbose_name="Comida diaria")
    consumo_comida_rapida = models.ForeignKey(consumo_comida_rapida, on_delete=models.CASCADE,default=1, verbose_name="Consumo de comida rápida")
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE,default=1,verbose_name="Clasificación de peso")  
    is_delete = models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def clean(self):
        if self.edad is None or not (13 <= self.edad <= 18):
            raise ValidationError("La edad debe estar entre 13 y 18 años.")
        if self.peso is None or self.peso <= 0:
            raise ValidationError("El peso debe ser un número positivo.")
        if self.estatura is None or self.estatura <= 0:
            raise ValidationError("La estatura debe ser un número positivo.")

    def save(self, *args, **kwargs):
        if self.peso and self.estatura:
            self.imc = round(float(self.peso) / (float(self.estatura) ** 2), 1)
            if self.imc < 18.5:
                self.clasificacion_id = 1
            elif 18.5 <= self.imc <= 24.9:
                self.clasificacion_id = 2
            elif 25.0 <= self.imc <= 29.9:
                self.clasificacion_id = 3
            elif 30.0 <= self.imc <= 34.9:
                self.clasificacion_id = 4
            elif 35.0 <= self.imc <= 39.9:
                self.clasificacion_id = 5
            else:
                self.clasificacion_id = 6
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_completo
    class Meta:
        verbose_name = "DATOS DE PERSONAS"
        verbose_name_plural = "DATOS DE PERSONAS"

