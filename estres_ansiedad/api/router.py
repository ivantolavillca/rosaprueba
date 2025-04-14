from rest_framework.routers import DefaultRouter
from estres_ansiedad.api.views import EstresAnsiedadApiViewSet

router_estres_ansiedad = DefaultRouter()

router_estres_ansiedad.register(prefix='estres-ansiedad', basename='estres ansiedad', viewset=EstresAnsiedadApiViewSet)