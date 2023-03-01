from django import forms
from .models import Livros, Categoria


class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'
        # exclude = ['usuario', 'data_cadastro']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_cadastro'].widget.attrs['readonly'] = True
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'autocomplete': 'off'})

        self.fields['emprestado'].widget.attrs.update({'style': 'width: 20px; height: 20px;'})

        self.fields['usuario'].widget = forms.HiddenInput()


class CadastroCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['usuario'].widget = forms.HiddenInput()

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'autocomplete': 'off'})