from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'email', 'username', 'password']
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        token['username'] = f"{user.first_name} {user.last_name}".upper() 
        token['email'] = user.email
        token['groups'] = list(user.groups.values_list('name', flat=True))  
        return token
class UserApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']