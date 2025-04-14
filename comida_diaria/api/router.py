from rest_framework.routers import DefaultRouter
from comida_diaria.api.views import ComidaDiariaApiViewSet

router_comida_diaria = DefaultRouter()

router_comida_diaria.register(prefix='comida-diaria', basename='comida diaria', viewset=ComidaDiariaApiViewSet)