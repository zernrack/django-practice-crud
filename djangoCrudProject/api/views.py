from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

# Create your views here.
@api_view(['GET'])
def get_users(request):
    user = User.objects.all()
    serialized = UserSerializer(user, many=True)
    return Response(serialized.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    ...