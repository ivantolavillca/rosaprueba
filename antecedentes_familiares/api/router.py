from rest_framework.routers import DefaultRouter
from antecedentes_familiares.api.views import AntecedentesFamiliaresApiViewSet

router_antecedentes_familiares = DefaultRouter()

router_antecedentes_familiares.register(prefix='antecedentes-familiares', basename='antecedentes familiares', viewset=AntecedentesFamiliaresApiViewSet)