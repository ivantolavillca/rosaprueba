from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from personas.api.permissions import IsAdminOrReadOnly
from personas.api.serializers import PersonaSerializer, ReportPersonaSerializer
from personas.models import Personas
from rest_framework.pagination import PageNumberPagination

class PersonaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Personas.objects.filter(is_delete=False)
    serializer_class = PersonaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre_completo', 'edad', 'peso', 'estatura']
    pagination_class = PageNumberPagination
    page_size = 10
    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Persona eliminada exitosamente."},
            status=status.HTTP_200_OK
        )
class ExportDataView(APIView):
    def get(self, request, format=None):
        # Filtra los datos del modelo
        queryset = Personas.objects.filter(is_delete=False)
        # Serializa los datos
        serializer = ReportPersonaSerializer(queryset, many=True)
        serialized_data = serializer.data
        # Convierte los datos serializados a un DataFrame de Pandas
        data = pd.DataFrame(serialized_data)
        # Obtén el formato de salida (Excel o CSV)
        output_format = request.query_params.get('format', 'csv')
        if output_format == 'excel':
            # Crea un archivo Excel
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
            with pd.ExcelWriter(response, engine='openpyxl') as writer:
                data.to_excel(writer, index=False)
        else:
            # Crea un archivo CSV
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            data.to_csv(response, index=False)
        return response