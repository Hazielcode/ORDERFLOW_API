from django.db import models

# Modelo que representa un cliente del sistema
class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("pagado", "Pagado"),
        ("enviado", "Enviado"),
        ("cancelado", "Cancelado"),
    ]

    fecha = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente} ({self.estado})"
