from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from todorestapi.models import Task
from todorestapi.serializers import TaskSerializer
from rest_framework import status



@api_view(['GET'])
def get_all_to_do_items(request):
    tasks = Task.objects.all()
    serialized_tasks = TaskSerializer(tasks,many=True)
    return Response(serialized_tasks.data)
@api_view(['GET'])



def get_specific_to_do_item(request,id):
    required_task = Task.objects.get(pk=id)
    serialized_required_task = TaskSerializer(required_task)
    return Response(serialized_required_task.data)



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
    


@api_view(['DELETE'])
def remove_an_item(request,id):
    try:
        Task.objects.get(pk=id).delete()
        return Response({"message":"required object delete"})
    except Exception as e:
        return Response({"message":"could not delete"})