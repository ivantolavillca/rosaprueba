from django.db import models
class Clasificacion(models.Model):
    nombre=models.CharField(max_length=50)
    is_delete= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
