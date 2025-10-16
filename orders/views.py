from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Cliente, Pedido
from .serializers import ClienteSerializer, PedidoSerializer

# CRUD completo para la entidad Cliente, con búsqueda por nombre/dirección/email
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]
    search_fields = ["nombre", "direccion", "email", "telefono"]


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.select_related("cliente").all()
    serializer_class = PedidoSerializer
    permission_classes = [AllowAny]
    search_fields = ["estado", "cliente__nombre"]
    filterset_fields = ["estado", "cliente"]
