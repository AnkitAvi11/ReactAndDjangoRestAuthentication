from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Task

#   defifing the serializer for the tasks
class TaskSerializer(serializers.ModelSerializer) : 

    class Meta : 
        model = Task 
        fields = [
            'id', 
            'user',
            'title', 
            'dscription',
            'created_on'
        ]

        read_only_fields = [
            'created_on',
            'user'
        ]

class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = User
        fields = [
            'id', 
            'username',
            'email'
        ]

        read_only_fields = [
            'email'
        ]