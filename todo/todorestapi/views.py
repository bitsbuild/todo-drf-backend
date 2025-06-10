from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
def sample(request):
    return HttpResponse("Sample Works Well")