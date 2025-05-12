from rest_framework import viewsets 
from loja.api import serialiser
from loja import models 
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import F, Sum


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serialiser.CategoriaSerializer
    queryset = models.Categoria.objects.all()

    @swagger_auto_schema(
        operation_description="Lista todas as categorias disponíveis",
        responses={200: serialiser.CategoriaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria uma categoria conforme os dados passados",
        responses={201: serialiser.CategoriaSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna a categoria conforme o ID informado",
        responses={200: serialiser.CategoriaSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Altera dados de uma categoria conforme ID e dados passados",
        responses={200: serialiser.CategoriaSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Deleta uma categoria conforme o ID informado",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = serialiser.ProdutoSerializer
    queryset = models.Produto.objects.all()

    @swagger_auto_schema(
        operation_description="Lista todos os produtos disponíveis",
        responses={200: serialiser.ProdutoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria um produto conforme os dados passados",
        responses={201: serialiser.ProdutoSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o produto conforme o ID informado",
        responses={200: serialiser.ProdutoSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Altera dados de um produto conforme ID e dados passados",
        responses={200: serialiser.ProdutoSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Deleta um produto conforme o ID informado",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


