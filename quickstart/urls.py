from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'funcionarios/', views.ListaFuncionarios.as_view(), name='funcionarios-list'),

]