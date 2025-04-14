from django.contrib import admin
from genero.models import genero
@admin.register(genero)
class generoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "ADMINISTRACIÓN DE GÉNERO"
admin.site.site_title = "GESTIÓN DE GÉNERO"
admin.site.index_title = "ADMINISTRACIÓN Y GESTIÓN DE GÉNERO"