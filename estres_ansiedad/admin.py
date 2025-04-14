from django.contrib import admin

from estres_ansiedad.models import estres_ansiedad
@admin.register(estres_ansiedad)
class estres_ansiedadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "ADMINISTRACIÓN DE ESTRÉS Y ANSIEDAD"
admin.site.site_title = "ESTRÉS Y ANSIEDAD"
admin.site.index_title = "GESTIÓN DE ESTRÉS Y ANSIEDAD"