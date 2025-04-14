from django.contrib import admin
from condiciones_medicas.models import condiciones_medicas
@admin.register(condiciones_medicas)
class condiciones_medicasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "ADMINISTRACIÓN DE CONDICIONES MÉDICAS"
admin.site.site_title = "CONDICIONES MÉDICAS"
admin.site.index_title = "GESTIÓN DE CONDICIONES MÉDICAS"