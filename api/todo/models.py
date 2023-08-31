from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 20)

    def __str__(self):
        return f'Nome: {self.nome}'

class TodoList(models.Model):
    tarefa = models.CharField(max_length= 20)
    choices_status = [ #o primeiro valor entra no banco de dados, o segundo aparece para o usuario
        ('C', 'concluido'),
        ('E_A', 'em andamento'),
        ('P', 'pendente'),
    ]
    status = models.CharField(choices = choices_status, max_length = 12)
    pessoa = models.ForeignKey( #chave utilizada para relacionar uma tabela a outra no banco de dados
        Pessoa,
        max_length = 20,
        on_delete = models.CASCADE
    )