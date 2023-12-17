from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


# Create your views here.
# In this case I do not need views. I will use it for my controllers

# GET methods - get the data from json Postman body, serializes it and prints
# serializes the instance with (many arg=T/F)
@api_view(['GET'])
def get_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': f'An error occurred. Details: {str(e)}'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_user(request, pk):
    try:
        users = User.objects.get(id=pk)
        serializer = UserSerializer(users, many=False)
        return Response({"status": "success", "user": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'User not found'},
                        status=status.HTTP_404_NOT_FOUND)


# POST method - create user with give data from json body - Postman or similar
# Uses only the serializer if it's valid
@api_view(['POST'])
def create_user(request):
    try:
        # Check if a user with the same name and email already exists
        existing_user = User.objects.filter(
            email=request.data.get('email')).first()

        if existing_user:
            return Response({'error': 'User with same email already exists.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # If not existing user is false, keep going with creating one
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid data provided'},
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': f'An error occurred. Details: {str(e)}'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
# PUT method - gets already created instance and updates it if is valid
def update_user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({'error': 'User not found!'},
                        status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(instance=user, data=request.data)

    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'success', 'user': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": f'Invalid data provided. Details: {str(e)}'},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
# DELETE method - if user is existing delete it
def delete_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        user.delete()
        return Response("User successfully deleted!")
    except Exception as e:
        return Response({"error": f"User with id:{pk} doesn't exist"},
                        status=status.HTTP_404_NOT_FOUND)
