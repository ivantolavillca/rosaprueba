from django.db import models

class estres_ansiedad(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Sufre de estres o ansiedad?")
    is_delete= models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "ESTRES O ANSIEDAD"
        verbose_name_plural = "ESTRES O ANSIEDAD"
