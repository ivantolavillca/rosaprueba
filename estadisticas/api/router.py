from django.urls import path
from estadisticas.api.view import GeneroCountView, PesoPorEdadView, EstaturaPorEdadView, ImcPorEdadView, ClasificacionPorEdadView,EdadPorClasificacionView,ConteoPorClasificacionView

urlpatterns = [
    path('peso-por-edad/', PesoPorEdadView.as_view(), name='peso-por-edad'),
    path('estatura-por-edad/', EstaturaPorEdadView.as_view(), name='estatura-por-edad'),
    path('imc-por-edad/', ImcPorEdadView.as_view(), name='imc-por-edad'),
    path('clasificacion-por-edad/', ClasificacionPorEdadView.as_view(), name='clasificacion-por-edad'),
    path('edad-por-clasificacion/', EdadPorClasificacionView.as_view(), name='edad-por-clasificacion'),
    path('cantidad-genero', GeneroCountView.as_view(), name='cantidad-genero'),
    path('pesonas-clasificacion', ConteoPorClasificacionView.as_view(), name='pesonas-clasificacion'),
]