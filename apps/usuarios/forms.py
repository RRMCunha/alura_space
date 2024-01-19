from django import forms

class LoginForms(forms.Form):
    nome_usuario=forms.CharField(
        label='Usuário', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_usuario=forms.CharField(
        label='Usuário', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva',
            }
        )
    )

    nome_primeiro_cadastro=forms.CharField(
        label='Primeiro Nome', 
        required=False, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João',
            }
        )
    )

    nome_ultimo_cadastro=forms.CharField(
        label='Último Nome', 
        required=False, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: da Silva',
            }
        )
    )

    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        )
    )

    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite uma senha válida',
            }
        ),
    )

    senha_2=forms.CharField(
        label='Confirme a senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha novamente',
            }
        ),
    )

    def clean_nome_usuario(self):
        nome = self.cleaned_data.get('nome_usuario')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('ATENÇÃO: Não são permitidos espaços neste campo!!!')
            else:
                return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais!!!')
            else:
                return senha_2