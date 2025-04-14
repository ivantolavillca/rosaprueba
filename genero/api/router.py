from rest_framework.routers import DefaultRouter
from genero.api.views import GeneroApiViewSet

router_genero = DefaultRouter()

router_genero.register(prefix='genero', basename='genero', viewset=GeneroApiViewSet)