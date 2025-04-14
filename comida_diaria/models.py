from django.db import models

class comida_diaria(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Cuantas veces consume comida diaria?")
    is_delete= models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "CONSUMO DE COMIDA DIARIA"
        verbose_name_plural = "CONSUMO DE COMIDA DIARIA"
