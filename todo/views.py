from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.middleware.csrf import get_token
from django.http import JsonResponse

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})