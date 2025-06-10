from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
def sample(request):
    return HttpResponse("Sample Works Well")