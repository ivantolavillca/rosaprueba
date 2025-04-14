from django.contrib import admin
from actividades_fisicas.models import ActividadesFisicas
@admin.register(ActividadesFisicas)
class ActividadesFisicasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "ADMINISTRACIÓN DE ACTIVIDADES FÍSICAS"
admin.site.site_title = "ACTIVIDADES FÍSICAS"
admin.site.index_title = "GESTIÓN DE ACTIVIDADES FÍSICAS"
