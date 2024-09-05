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
    
@api_view(['GET','PUT','DELETE'])
def user_details(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serialized = UserSerializer(user)
        return Response(serialized.data)
    elif request.method == "PUT":
        serialized = UserSerializer(user, data=request.data)
        serialized.is_valid()
        serialized.save()
        return Response(serialized.data)
    elif request.method == "DELETE":
        user.delete()
        redirect()
        return Response(status=status.HTTP_204_NO_CONTENT)
        