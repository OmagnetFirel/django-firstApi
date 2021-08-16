from rest_framework import generics
from .models import Funcionario
from .serializers import FuncionarioSerializer

# Create your views here.

class ListaFuncionarios(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    