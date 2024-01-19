from django.urls import path
from apps.galeria.views import \
    index, imagem, buscar, nova_foto, editar_foto, deletar_foto

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-foto', nova_foto, name='nova_foto'),
    path('editar-foto/<int:foto_id>', editar_foto, name='editar_foto'),
    path('deletar-foto/<int:foto_id>', deletar_foto, name='deletar_foto'),
]