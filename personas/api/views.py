from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from personas.api.permissions import IsAdminOrReadOnly
from personas.api.serializers import PersonaSerializer, ReportPersonaSerializer,ModeloDatos
from personas.models import Personas
from rest_framework.pagination import LimitOffsetPagination
import os
from django.conf import settings
import tensorflow as tf
import numpy as np
import joblib
#model_path = os.path.join(settings.BASE_DIR, 'personas', 'obesidad_model.keras')
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
model_path = os.path.join(settings.BASE_DIR, 'personas', 'obesidad_model.keras')
scaler_path = os.path.join(settings.BASE_DIR, 'personas', 'scaler.pkl')
label_encoder_path = os.path.join(settings.BASE_DIR, 'personas', 'label_encoder.pkl')
model = tf.keras.models.load_model(model_path)
scaler = joblib.load(scaler_path)
label_encoder = joblib.load(label_encoder_path)
class PredecirObesidadView(APIView):
    def post(self, request):
        serializer = ModeloDatos(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        edad = serializer.validated_data['edad']
        peso = serializer.validated_data['peso']
        estatura = serializer.validated_data['estatura']
        imc = peso / (estatura ** 2)
        datos_entrada = pd.DataFrame({
            'edad': [edad],
            'peso': [peso],
            'estatura': [estatura],
            'imc': [imc]
        })
       # datos_entrada = np.array([[edad, peso, estatura, imc]], dtype=np.float32)
        datos_entrada = scaler.transform(datos_entrada) 
        try:
           prediccion = model.predict(datos_entrada)
           prediccion_clase = np.argmax(prediccion, axis=1)  
           resultado = int(prediccion_clase[0]) 
           clasificacion = label_encoder.inverse_transform([resultado])[0]
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'prediccion': clasificacion}, status=status.HTTP_200_OK)

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10  # Número de registros por defecto
    max_limit = 100  # Límite máximo de registros
class PersonaApiViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    queryset = Personas.objects.filter(is_delete=False)
    serializer_class = PersonaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre_completo', 'edad', 'peso', 'estatura']
    pagination_class = CustomLimitOffsetPagination 
    
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