from rest_framework import serializers
from .models import Cliente, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nombre", "direccion", "email", "telefono"]

"""Serializador para la entidad Cliente."""
#commit relleno xd
class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    cliente_detalle = ClienteSerializer(source="cliente", read_only=True)
    cliente_nombre = serializers.CharField(source="cliente.nombre", read_only=True)

    class Meta:
        model = Pedido
        fields = [
            "id",
            "fecha",
            "monto_total",
            "estado",
            "cliente",          # se envía el id del cliente
            "cliente_detalle",  # muestra todo el cliente relacionado
            "cliente_nombre",   # campo personalizado (+1 punto extra)
        ]
