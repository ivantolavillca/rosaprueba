from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from clasificacion_peso.api.permissions import IsAdminOrReadOnly
from clasificacion_peso.api.serializers import ClasificacionSerializer
from personas.models import Personas
import pandas as pd

class PesoPorEdadView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        data = Personas.objects.filter(is_delete=False).values('edad', 'peso')
        df = pd.DataFrame(data)
        estadisticas = df.groupby('edad')['peso'].describe().to_dict()
        return Response(estadisticas, status=status.HTTP_200_OK)

class EstaturaPorEdadView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        data = Personas.objects.filter(is_delete=False).values('edad', 'estatura')
        df = pd.DataFrame(data)
        estadisticas = df.groupby('edad')['estatura'].describe().to_dict()
        return Response(estadisticas, status=status.HTTP_200_OK)

class ImcPorEdadView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        data = Personas.objects.filter(is_delete=False).values('edad', 'imc')
        df = pd.DataFrame(data)
        estadisticas = df.groupby('edad')['imc'].describe().to_dict()
        return Response(estadisticas, status=status.HTTP_200_OK)

class ClasificacionPorEdadView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        data = Personas.objects.filter(is_delete=False).values('edad', 'clasificacion')
        df = pd.DataFrame(data)
        estadisticas = df.groupby('edad')['clasificacion'].describe().to_dict()
        return Response(estadisticas, status=status.HTTP_200_OK)
class ClasificacionPorGeneroView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        data = Personas.objects.filter(is_delete=False).values('genero', 'clasificacion')
        df = pd.DataFrame(data)
        estadisticas = df.groupby('genero')['clasificacion'].describe().to_dict()
        return Response(estadisticas, status=status.HTTP_200_OK)
class EdadPorClasificacionView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        data = Personas.objects.filter(is_delete=False).values('clasificacion', 'edad')
        df = pd.DataFrame(data)
        estadisticas = df.groupby('clasificacion')['edad'].describe().fillna(0).to_dict()
        return Response(estadisticas, status=status.HTTP_200_OK)

class GeneroCountView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        data = Personas.objects.filter(is_delete=False).values('genero')
        df = pd.DataFrame(data)
        conteo = df['genero'].value_counts().to_dict()
        return Response(conteo, status=status.HTTP_200_OK)
class ConteoPorClasificacionView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        data = Personas.objects.filter(is_delete=False).values('clasificacion')
        df = pd.DataFrame(data)
        conteo = df['clasificacion'].value_counts().to_dict()
        return Response(conteo, status=status.HTTP_200_OK)