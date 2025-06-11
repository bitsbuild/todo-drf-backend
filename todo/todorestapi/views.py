from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from todorestapi.models import Task
from todorestapi.serializers import TaskSerializer,AddSerializer,UpdateSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

# Completed
@api_view(['GET'])    
def get_all_to_do_items(request):
    tasks = Task.objects.all()
    serialized_tasks = TaskSerializer(tasks,many=True)
    return Response(serialized_tasks.data)


#Completed
@api_view(['GET'])
def get_specific_to_do_item(request,id):
    required_task = Task.objects.get(pk=id)
    serialized_required_task = TaskSerializer(required_task)
    return Response(serialized_required_task.data)

#Completed
@swagger_auto_schema(method='post',request_body=AddSerializer)
@api_view(['POST'])
def add_an_item(request):
    try:    
        name = request.data.get('name')
        desc = request.data.get('desc')
        Task.objects.create(
            task_name=name,
            task_description=desc
        )
        return Response({"Status":"Task Creation Successfully"},status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"Status":"Task Creation Failed"},status=status.HTTP_400_BAD_REQUEST)


#Completed
@swagger_auto_schema(method='put',request_body=UpdateSerializer)
@api_view(['PUT'])
def update_an_item(request,id):
    try:
        name = request.data.get('name')
        desc = request.data.get('desc')
        task_to_update = Task.objects.get(pk=id)
        task_to_update.task_name = name
        task_to_update.task_description = desc
        task_to_update.save()
        return Response({"message":"task update successful"},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message":"task update failed"},status=status.HTTP_400_BAD_REQUEST)
    

#Completed
@api_view(['DELETE'])
def remove_an_item(request,id):
    try:
        Task.objects.get(pk=id).delete()
        return Response({"message":"required object deleted"})
    except Exception as e:
        return Response({"message":"could not delete"})


#Completed
@api_view(['PUT'])
def mark_as_done(request,id):
    try:
        task = Task.objects.get(pk=id)
        task.is_completed = True
        task.save()
        return Response({"message":"task marked done"},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message":"task marking failed","error":str(e)},status=status.HTTP_400_BAD_REQUEST)