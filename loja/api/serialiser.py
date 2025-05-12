from rest_framework import serializers
from loja import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = "__all__"
        extra_kwargs={
            'id' : {'help_text':'Identificador do mostruário'},
            'nome': {'help_text': 'nome do produto'},
            'Descricao':{'help_text': 'Descrição do que mostruario'},
            'Preco':{'help_text': 'preço da roupa'},
            'Foto': {'help_text': 'Foto da roupa'}
            }
        
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produto
        fields = "__all__"
        extra_kwargs={
             'id' : {'help_text':'Identificador o Produto'},
            'nome': {'help_text': 'nome do produto'},
            'Descricao':{'help_text': 'Descrição do que mostruario'},
            'Preco':{'help_text': 'preço da roupa'},
            'imagem': {'help_text': 'Imagem da roupa'},
            'categoriaid':{'help_text':'categoria do produto'}
            }