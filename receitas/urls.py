from django.urls import path 

from .views import ReceitasAPIView

urlpatterns = [
    path('receitas/', ReceitasAPIView.as_view(), name='receitas'),

]

