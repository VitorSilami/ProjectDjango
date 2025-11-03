#Isolando o arquivo galeria/urls.py(Boa prática para organização de URLs em apps Django)

from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]
