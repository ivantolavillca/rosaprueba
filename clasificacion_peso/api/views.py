from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from clasificacion_peso.api.permissions import IsAdminOrReadOnly
from clasificacion_peso.api.serializers import ClasificacionSerializer
from clasificacion_peso.models import Clasificacion
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
# class CustomPagination(PageNumberPagination):
#     page_size = 2 
#     page_size_query_param = 'page_size'  
#     max_page_size = 10  
class ClasificacionApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Clasificacion.objects.filter(is_delete=False)
    serializer_class = ClasificacionSerializer
    filter_backends = [SearchFilter]
    #filterset_fields = ['nombre_completo','edad','peso','estatura']
    search_fields = ['nombre']
   # pagination_class = CustomPagination 
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Persona creada exitosamente."},
            status=status.HTTP_200_OK
        )

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Persona actualizada exitosamente."},
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete=True
        instance.save()
        #self.perform_destroy(instance)
        return Response(
            {"message": "Persona eliminada exitosamente."},
            status=status.HTTP_200_OK
        )

    #lookup_field = 'slug'
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['nombre_completo', 'peso','edad']