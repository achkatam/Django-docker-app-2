# I do not need views, it's API app so I'll create controllers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer


# GET methods - 'many' funcs
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


# POST method - just serializer - serializes the given data for the model
@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    return Response(serializer.data)


# PUT method - instance of the model with given data
@api_view(["PUT"])
def update_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    return Response(serializer.data)


# DELETE method - just the model
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response("Deleted!")
