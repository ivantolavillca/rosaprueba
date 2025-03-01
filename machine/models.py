from django.db import models

class MachineModel(models.Model):
    
    description = models.TextField(null=True, blank=True)
    model_file = models.FileField(upload_to='models/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name