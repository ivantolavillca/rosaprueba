from django.contrib import admin
from consumo_comida_rapida.models import consumo_comida_rapida
@admin.register(consumo_comida_rapida)
class consumo_comida_rapidaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "ADMINISTRACIÓN DE CONSUMO DE COMIDA RÁPIDA"
admin.site.site_title = "CONSUMO DE COMIDA RÁPIDA"
admin.site.index_title = "GESTIÓN DE CONSUMO DE COMIDA RÁPIDA"