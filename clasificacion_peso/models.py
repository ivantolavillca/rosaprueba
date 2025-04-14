from django.db import models
class Clasificacion(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre de la clasificación")
    is_delete= models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "CLASIFICACION DE PESO"
        verbose_name_plural = "CLASIFICACION DE PESO"
