from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters

# Create your views here.
from .models import Pedidos, ItensPedido
from .serializers import PedisoSerializer, ItemPedidoSerializer


class PedidosListView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):

    queryset = Pedidos.objects.all()
    serializer_class = PedisoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'nome')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PedidosDetailView(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):

    queryset = Pedidos.objects.all()
    serializer_class = PedisoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'nome')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ItensPedidosListView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):

    queryset = ItensPedido.objects.all()
    serializer_class = ItemPedidoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'nome')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ItensPedidosDetailView(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):

    queryset = ItensPedido.objects.all()
    serializer_class = ItemPedidoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'nome')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
