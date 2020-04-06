from rest_framework import serializers

from .models import Pedidos, ItensPedido


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = ('id', 'produtos', 'pedido_id')


class PedisoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedidos
        fields = ('id', 'cod_cliente', 'total_pedido', 'itens')

    def create(self, validated_data):
        itens = validated_data.pop('itens')
        pedido = Pedidos.objects.create(**validated_data)
        for item in itens:
            ItensPedido.objects.create(pedido=pedido, **item)
        return pedido

