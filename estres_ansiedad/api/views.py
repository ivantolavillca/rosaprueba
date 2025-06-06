from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from estres_ansiedad.api.permissions import IsAdminOrReadOnly
from estres_ansiedad.api.serializers import EstresAnsiedadSerializer
from estres_ansiedad.models import estres_ansiedad
from rest_framework.filters import SearchFilter

class EstresAnsiedadApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = estres_ansiedad.objects.filter(is_delete=False)
    serializer_class = EstresAnsiedadSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Estres o ansiedad creada exitosamente."},
            status=status.HTTP_200_OK
        )

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Estres o ansiedad actualizada exitosamente."},
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete=True
        instance.save()
        return Response(
            {"message": "Estres o ansiedad eliminada exitosamente."},
            status=status.HTTP_200_OK
        )
