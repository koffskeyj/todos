from django.shortcuts import render
from rest_framework import generics
from todo.serializers import TodoSerializer
from todo.models import Todo

import json

class TodoListAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
