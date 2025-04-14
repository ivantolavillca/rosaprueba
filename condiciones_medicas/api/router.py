from rest_framework.routers import DefaultRouter
from condiciones_medicas.api.views import CondicionesMedicasApiViewSet

router_condicion_medica = DefaultRouter()

router_condicion_medica.register(prefix='condicion-medica', basename='condicion medica', viewset=CondicionesMedicasApiViewSet)