# from django.shortcuts import render
from rest_framework import viewsets #importa as viewsets
from .models import TodoList, Pessoa #importa as classes TodoList e Pessoa q foi criada
from .serializers import TodoListSerializer, PessoaSerializer #importa as classes serializadas para json

# Create your views here.
class TodoListViewset(viewsets.ModelViewSet):
    
    #consulta todas as instancias da TodoList
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer