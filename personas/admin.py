from django.contrib import admin
from .models import Personas

@admin.register(Personas)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo','genero', 'edad', 'peso', 'estatura', 'imc', 'clasificacion', 'created_at']
    list_filter = ['clasificacion']

    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()

    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
