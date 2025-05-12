from django.db import models
import os
import uuid
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible 
class RenameImage(object):
    def __init__(self, subdir='produto'):
        self.subdir= subdir

    def __call__(self, instance,filename):
        extension = filename.split('.')[-1]
        new_name = f"{uuid.uuid4()}.{extension}"
        return os.path.join(self.subdir, new_name)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.ImageField(upload_to=RenameImage('categoria/'))
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to=RenameImage('produtos/'))
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoriaid = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)



