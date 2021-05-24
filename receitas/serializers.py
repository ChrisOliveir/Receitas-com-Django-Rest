from django.db.models import fields
from rest_framework import serializers

from .models import Receitas

class ReceitasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receitas
        fields = (
            'nome_receita',
            'ingredientes',
            'modo_preparo'

        )