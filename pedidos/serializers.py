from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Pedidos, ItensPedido


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = ('id', 'produtos', 'pedido_id')


class PedisoSerializer(serializers.ModelSerializer):
    # items_display = serializers.SerializerMethodField('get_item')
    itens = ItemPedidoSerializer()

    class Meta:
        model = Pedidos
        fields = ('id', 'cod_cliente', 'total_pedido', 'itens')

# def get_item(self, obj):
#    return PedisoSerializer(obj.pedido_id).data

