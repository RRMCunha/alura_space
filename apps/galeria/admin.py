from django.contrib import admin
from apps.galeria.models import Foto

class ListandoFotos(admin.ModelAdmin):
    list_display = ("id", "titulo", "legenda", "publicada")
    list_display_links = ("id", "titulo")
    search_fields = ("titulo",)
    list_filter = ("categoria", 'usuario')
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Foto, ListandoFotos)
