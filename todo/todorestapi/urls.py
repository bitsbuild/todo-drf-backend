from django.urls import path
from todorestapi.views import sample
urlpatterns = [
    path('sample',sample)
]

