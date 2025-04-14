from rest_framework.routers import DefaultRouter
from actividades_fisicas .api.views import ActividadesFisicasApiViewSet

router_actividades_fisicas = DefaultRouter()

router_actividades_fisicas.register(prefix='actividades-fisicas', basename='actividades fisicas', viewset=ActividadesFisicasApiViewSet)