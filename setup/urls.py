
from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from loja.api import viewsets


route = routers.DefaultRouter()
route.register(r'categoria', viewsets.CategoriaViewSet, basename="Categoria")
route.register(r'produto', viewsets.ProdutoViewSet, basename="Produto")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)