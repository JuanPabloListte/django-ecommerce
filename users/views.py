from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from . models import User
from . serializers import RegisterUserSerializer, MyTokenObteinPairSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from backend.pagination import CustomPagination

@api_view(['POST'])
def register(request):
    data = request.data
    user = User.objects.create(
        email = data['email'],
        name = data['name'],
        last_name = data['last_name'],
        password = make_password(data['password'])
    )
    serializer = RegisterUserSerializer(user, many=False)
    return Response(serializer.data)


    
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.all()
    paginator = CustomPagination()
    paginated_users = paginator.paginate_queryset(users, request)
    serializer = UserSerializer(paginated_users, many=True)
    return paginator.get_paginated_response(serializer.data)


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObteinPairSerializer

