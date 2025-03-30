from django.db import models
from clasificacion_peso.models import Clasificacion
from django.db.models import CASCADE
from django.core.exceptions import ValidationError
class Personas(models.Model):
    nombre_completo = models.CharField(max_length=255)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    estatura = models.DecimalField(max_digits=10, decimal_places=2)
    imc = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    genero = models.CharField(max_length=255,null=True,blank=True)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, null=True, blank=True)
    is_delete= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
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
                self.clasificacion_id = 1  # Bajo peso
            elif 18.5 <= self.imc <= 24.9:
                self.clasificacion_id = 2  # Normal
            elif 25.0 <= self.imc <= 29.9:
                self.clasificacion_id = 3  # Sobrepeso
            elif 30.0 <= self.imc <= 34.9:
                self.clasificacion_id = 4  # Obesidad I
            elif 35.0 <= self.imc <= 39.9:
                self.clasificacion_id = 5  # Obesidad II
            else:
                self.clasificacion_id = 6  # Obesidad III
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_completo

