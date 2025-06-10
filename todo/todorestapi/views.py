from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def sample(request):
    return HttpResponse("Sample Works Well")
@api_view(['GET'])
def get_all_to_do_items(request):
    return HttpResponse("")
@api_view(['GET'])
def get_specific_to_do_item(request):
    return HttpResponse("")
@api_view(['POST'])
def add_an_item(request):
    return HttpResponse("")
@api_view(['PUT'])
def update_an_item(request):
    return HttpResponse("")
@api_view(['DELETE'])
def remove_an_item(request):
    return HttpResponse("")
