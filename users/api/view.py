from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from users.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.viewsets import ModelViewSet
from personas.api.permissions import IsAdminOrReadOnly
from rest_framework.filters import SearchFilter
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ValidateTokenView(APIView):
    def post(self, request):
        token = request.data.get("token")
        if not token:
            return Response({"isSuccess": False}, status=400)
        try:
            AccessToken(token)  # Valida el token
            return Response({"isSuccess": True},status=200)
        except Exception:
            return Response({"isSuccess": False}, status=401)
        
class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all().order_by('last_name')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
# class UserApiViewSet(ModelViewSet):
#     permission_classes = [IsAdminOrReadOnly]
#     queryset = User.objects.filter(is_delete=False)
#     serializer_class = UserSerializer
#     filter_backends = [SearchFilter]
    #filterset_fields = ['nombre_completo','edad','peso','estatura']
   # search_fields = ['nombre_completo', 'edad', 'peso', 'estatura']
   # pagination_class = CustomPagination 
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(
    #         {"message": "Persona creada exitosamente."},
    #         status=status.HTTP_200_OK
    #     )

    # def put(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(
    #         {"message": "Persona actualizada exitosamente."},
    #         status=status.HTTP_200_OK
    #     )

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.is_delete=True
    #     instance.save()
    #     #self.perform_destroy(instance)
    #     return Response(
    #         {"message": "Persona eliminada exitosamente."},
    #         status=status.HTTP_200_OK
    #     )