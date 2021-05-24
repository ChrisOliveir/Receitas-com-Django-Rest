from django.db import models

class Receitas(models.Model):
    nome_receita = models.CharField('nome', max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()


    def __str__(self):
        return self.nome_receita
