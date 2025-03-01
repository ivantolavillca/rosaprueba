from rest_framework.routers import DefaultRouter
from personas.api.views import PersonaApiViewSet

router_personas = DefaultRouter()

router_personas.register(prefix='personas', basename='personas', viewset=PersonaApiViewSet)