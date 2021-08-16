from django.db import models

# Create your models here.


class Funcionario(models.Model):
    class Meta:
        db_table = 'funcionario'
        
    nome = models.CharField(max_length=200)
    funcao = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome
    
    

