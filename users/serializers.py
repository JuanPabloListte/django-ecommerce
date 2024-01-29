from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from . models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'last_name', 'password']
        
        
class MyTokenObteinPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token ['email'] = user.email
        token ['avatar'] = user.avatar.url if user.avatar else None
        token ['is_staff'] = user.is_staff
        
        return token
    
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'email', 'avatar', 'is_staff', 'id']
