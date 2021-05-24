from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Receitas
from .serializers import ReceitasSerializer


class ReceitasAPIView(APIView):
    """
    API de receitas 
    """
    def get(self, request):
        receitas = Receitas.objects.all()
        serializer = ReceitasSerializer(receitas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        Serializer = ReceitasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response(Serializer.data, status=status.HTTP_201_CREATED)
