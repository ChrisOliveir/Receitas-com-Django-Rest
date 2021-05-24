from django.contrib import admin

from .models import Receitas

@admin.register(Receitas)

class ReceitasAdmin(admin.ModelAdmin):
    list_display = ('nome_receita','ingredientes','modo_preparo')


