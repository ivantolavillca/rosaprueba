from django.contrib import admin
from antecedentes_familiares.models import antecedentes_familiares
@admin.register(antecedentes_familiares)
class antecedentes_familiaresAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "ADMINISTRACIÓN DE ANTECEDENTES FAMILIARES"
admin.site.site_title = "ANTECEDENTES FAMILIARES"
admin.site.index_title = "GESTIÓN DE ANTECEDENTES FAMILIARES"
