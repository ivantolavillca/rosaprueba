"""
URL configuration for administrador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from drf_yasg.views import get_schema_view
from personas.api.router import router_personas
from clasificacion_peso.api.router import router_clasificacion
from django.views.generic.base import RedirectView
from personas.api.views import ExportDataView, PredecirObesidadView
schema_view = get_schema_view(
   openapi.Info(
      title="MEDIDAS API",
      default_version='v1',
      description="Documentación de la API del medidas para el modelo de machine learning",
      terms_of_service="",
      contact=openapi.Contact(email="rosa@gmail.com"),
      license=openapi.License(name="depgy solutions"),
   ),
   public=True,
   #authentication_classes=[TokenAuthentication],
  # permission_classes=[IsAuthenticated], 
   # permission_classes=(permissions.AllowAny,),
   
)

admin.site.site_header = "PROTOTIPO DE ADMINISTRACION DE CONTROL DE PESO"
admin.site.site_title = "Mi Sitio de Administración"
admin.site.index_title = "Bienvenido al Panel de Administración"
urlpatterns = [
    path('', RedirectView.as_view(url='/redocs/', permanent=False)),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include(router_personas.urls)),
    path('api/', include(router_clasificacion.urls)),
    path('api/', include('estadisticas.api.router')),
    path('api/report/persona/', ExportDataView.as_view(), name='export-data'),
    path('api/predecir-obesidad/', PredecirObesidadView.as_view(), name='predecir_obesidad'),
]
