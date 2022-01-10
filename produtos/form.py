from django.forms import ModelForm, fields
from django.forms.models import model_to_dict
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model= Produto
        fields = ['nome_produto','preco','unidade','publicador','descricao','foto']