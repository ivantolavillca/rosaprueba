from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from consumo_comida_rapida.api.permissions import IsAdminOrReadOnly
from consumo_comida_rapida.api.serializers import ConsumoComidaRapidaSerializer
from consumo_comida_rapida.models import consumo_comida_rapida
from rest_framework.filters import SearchFilter

class ConsumoComidaRapidaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = consumo_comida_rapida.objects.filter(is_delete=False)
    serializer_class = ConsumoComidaRapidaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Consumo de comida rapida creada exitosamente."},
            status=status.HTTP_200_OK
        )

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Consumo de comida rapida actualizada exitosamente."},
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete=True
        instance.save()
        return Response(
            {"message": "Consumo de comida rapida eliminada exitosamente."},
            status=status.HTTP_200_OK
        )
