from django import forms
from .models import Devolucao


class DevolucaoForm(forms.ModelForm):
    class Meta:
        model = Devolucao
        fields = [
            'codigo_produto',
            'marketplace',
            'motivo',
            'situacao',
            'data_devolucao',
            'observacao',
        ]
        widgets = {
            'data_devolucao': forms.DateInput(attrs={'type': 'date'}),
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }

    # coloca a classe do css em todos os campos pra ficar tudo igual
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'campo'
