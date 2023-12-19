from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


# Create your views here.

# get all users
@api_view(['GET'])
def get_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': f'An error occurred. Details: {str(e)}'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# get single user
@api_view(['GET'])
def get_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=200)
    except ObjectDoesNotExist:
        return Response({'error': 'User not found'},
                        status=status.HTTP_404_NOT_FOUND)


# add user
@api_view(['POST'])
def add_user(request):
    try:
        # Check if a user with the same name and email already exists
        existing_user = User.objects.filter(
            email=request.data.get('email')
        ).first()

        if existing_user:
            return Response({'error': 'User with the same email already exists'},
                            status=status.HTTP_400_BAD_REQUEST)

        # If no existing user, proceed with creating a new user
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


# update user
@api_view(["PUT"])
def update_user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(instance=user, data=request.data)

    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": f'Invalid data provided. Details: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)


# delete user
@api_view(["DELETE"])
def delete_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        user.delete()
        return Response("User successfully deleted!")
    except Exception as e:
        return Response({"error": f"User with id: {pk} doesn't exist"}, status=status.HTTP_404_NOT_FOUND)