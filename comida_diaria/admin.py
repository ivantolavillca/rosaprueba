from django.contrib import admin
from comida_diaria.models import comida_diaria
@admin.register(comida_diaria)
class comida_diariaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "ADMINISTRACIÓN DE COMIDA DIARIA"
admin.site.site_title = "COMIDA DIARIA"
admin.site.index_title = "GESTIÓN DE COMIDA DIARIA"