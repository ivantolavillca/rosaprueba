from django.contrib import admin
from consumo_medicamentos.models import consumo_medicamentos
@admin.register(consumo_medicamentos)
class consumo_medicamentosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "ADMINISTRACIÓN DE CONSUMO DE MEDICAMENTOS"
admin.site.site_title = "CONSUMO DE MEDICAMENTOS"
admin.site.index_title = "GESTIÓN DE CONSUMO DE MEDICAMENTOS"