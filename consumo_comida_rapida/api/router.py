from rest_framework.routers import DefaultRouter
from consumo_comida_rapida.api.views import ConsumoComidaRapidaApiViewSet

router_consumo_comida_rapida = DefaultRouter()

router_consumo_comida_rapida.register(prefix='consumo-comida-rapida', basename='consumo de comida rapida', viewset=ConsumoComidaRapidaApiViewSet)