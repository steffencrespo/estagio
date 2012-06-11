from django.db import models
from django.contrib.auth.models import User

class Aluno(User):
    data_ingresso = models.DateField()
    curso = models.CharField(max_length=50)
    
class Avaliador(User):
    pass

class Empresa(User):
    ramo_atuacao = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=20)
    avaliador = models.ForeignKey(Avaliador)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=16)

class Termo(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    aluno = models.ForeignKey(Aluno)
    empresa = models.ForeignKey(Empresa)
    aprovado = models.NullBooleanField()
    valor_bolsa = models.DecimalField(max_digits=10,decimal_places=2)
    funcao = models.CharField(max_length=50)
	
#o cliente quer uma tela de estatisticas de uso
#por user x logins no dia/no mes/no ano
#ideia - criar tabela que armazena referencia pro user e a data em um user fez login
#e depois criar uma view pra essa tabela pro user admin
#falta uma tela de welcome pra os usuarios fazerem login
#

class UserStats(models.Model):
#    avaliador = models.ForeignKey(Avaliador)
    data_login = models.DateField()