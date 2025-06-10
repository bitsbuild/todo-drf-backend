from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from todorestapi.models import Task
from todorestapi.serializers import TaskSerializer



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
    return HttpResponse("")



@api_view(['PUT'])
def update_an_item(request):
    return HttpResponse("")



@api_view(['DELETE'])
def remove_an_item(request):
    return HttpResponse("")