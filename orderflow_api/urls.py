from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views import PedidoViewSet, ClienteViewSet

router = DefaultRouter()
router.register(r"orders", PedidoViewSet, basename="orders")
router.register(r"clients", ClienteViewSet, basename="clients")

urlpatterns = [
    path("admin/", admin.site.urls),  # No usar admin como gestión
    path("api/", include(router.urls)),
]
