from rest_framework.routers import DefaultRouter
from consumo_medicamentos.api.views import ConsumoMedicamentosApiViewSet

router_consumo_medicamentos = DefaultRouter()

router_consumo_medicamentos.register(prefix='consumo-medicamentos', basename='consumo medicamentos', viewset=ConsumoMedicamentosApiViewSet)