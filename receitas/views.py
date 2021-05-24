from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Receitas
from .serializers import ReceitasSerializer

class Receitas(APIView):
    """
    API de receitas 
    """
    def get(self, request):
        receitas = Receitas.objects.all()
        serializer = ReceitasSerializer(receitas, many=True)
        return Response(serializer.data)