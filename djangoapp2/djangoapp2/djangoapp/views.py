from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


# Create your views here.
# In this case I do not need views. I will use it for my controllers

# GET methods - get the data from json Postman body, serializes it and prints
# serializes the instance with many arg=T/F
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# POST method - create user with give data from json body - Postman or similar
# Uses only the serializer if it's valid
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
# PUT method - gets already created instance and updates it if is valid
def update_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
# DELETE method - if user is existing delete it
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    return Response('Deleted successfully!')
