from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getalltasks(request) : 
    tasks = Task.objects.all().order_by('-created_on')
    serialized = TaskSerializer(tasks, many=True)

    return Response(
        serialized.data
    )


@api_view(['POST'])
def viewTask(request) : 
    id = request.POST.get('id')
    task = Task.objects.get(id=id)
    serialized = TaskSerializer(task) 
    return Response(
        serialized.data
    )

@api_view(['POST']) 
def createtask(request) : 
    try : 
        user = User.objects.get(id=request.POST.get('user'))
        title = request.POST.get('title')
        dscription = request.POST.get('dscription')

        task = Task.objects.create(user=user, title=title, dscription=dscription)

        serialized = TaskSerializer(task, many=False) 

        return Response(
            serialized.data
        )

    except Exception : 
        return Response('Some error occurred')


@api_view(['PATCH'])
def updateTask(request) : 
    try : 
        
        task_id = request.POST.get('task_id')
        print("TASK ID = ",task_id)

        task = Task.objects.get(id=task_id)
        serialised = TaskSerializer(task, data = {
            "title" : request.POST.get('title'),
            "dscription" : request.POST.get('dsc')
        })
        if serialised.is_valid() : 
            serialised.save()
            return Response(serialised.data)
        else : 
            return Response(serialised.errors)
    except Task.DoesNotExist:
        return Response({
            'error' : 'Task you are updating does not exist'
        })
    

@api_view(['POST'])
def loginUser(request) : 
    try : 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print("USER = ", user)
        if user is not None : 
            token, created = Token.objects.get_or_create(user=user)
            serialised = UserSerializer(user, many=False)
            return Response({
                'user' : serialised.data,
                'token' : token.key
            })
        else : 
            raise exceptions.ValidationError
    except User.DoesNotExist : 
        return Response({
            'message' : 'User doesnt '
        }, status=404)