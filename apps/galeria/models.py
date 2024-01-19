from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Foto(models.Model):

    OPCOES_CATEGORIA = [
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("NEBULOSA","Nebulosa"),
        ("PLANETA","Planeta"),
    ]

    titulo = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, blank=True, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=False)
    publicada = models.BooleanField(default=True)
    data_foto = models.DateTimeField(default=datetime.now, blank=True)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user'
    )

    def __str__(self):
        return self.titulo