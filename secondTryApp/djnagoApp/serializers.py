from rest_framework import serializers
from .models import User


class UserSerializer:
    class Meta:
        model = User
        fields = '__all__'