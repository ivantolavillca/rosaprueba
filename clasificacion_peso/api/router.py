from rest_framework.routers import DefaultRouter
from clasificacion_peso.api.views import ClasificacionApiViewSet

router_clasificacion = DefaultRouter()

router_clasificacion.register(prefix='clasificacion', basename='clasificacion', viewset=ClasificacionApiViewSet)