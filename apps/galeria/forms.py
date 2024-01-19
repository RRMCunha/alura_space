from django import forms
from apps.galeria.models import Foto

class FotoForms(forms.ModelForm):
    class Meta:
        model = Foto
        exclude = ['publicada',]
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'data_foto': 'Data de cadastro',
            'usuario': 'Usuário',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_foto': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }