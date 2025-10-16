# 🧩 ORDERFLOW_API

Proyecto hecho con **Django + Django REST Framework**, para manejar **clientes** y **pedidos** de forma sencilla.  
Cada pedido pertenece a un cliente, y todo se controla desde endpoints (no se usa el admin de Django).

---

## ⚙️ Instalación y ejecución

1. Clonar el proyecto:
   ```bash
   git clone https://github.com/Hazielcode/ORDERFLOW_API.git
   cd ORDERFLOW_API
Crear entorno virtual e instalar dependencias:

bash
Copiar código
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
Migrar y correr el servidor:

bash
Copiar código
python manage.py migrate
python manage.py runserver
El proyecto corre en:
👉 http://127.0.0.1:8000/api/

📦 Endpoints principales
🧍 CLIENTES /api/clients/
Método	Descripción	Ejemplo
GET	Lista todos los clientes	/api/clients/
POST	Crea un cliente nuevo	/api/clients/
PUT	Edita todos los datos de un cliente	/api/clients/1/
PATCH	Edita solo un campo	/api/clients/1/
DELETE	Elimina un cliente	/api/clients/1/

Ejemplo POST cliente:

json
Copiar código
{
  "nombre": "Juan Pérez",
  "direccion": "Av. Lima 123",
  "email": "juan@mail.com",
  "telefono": "999111222"
}
📦 PEDIDOS /api/orders/
Método	Descripción	Ejemplo
GET	Lista todos los pedidos	/api/orders/
POST	Crea un pedido nuevo	/api/orders/
PUT/PATCH	Actualiza pedido	/api/orders/1/
DELETE	Elimina pedido	/api/orders/1/
GET (search)	Busca por estado o cliente	/api/orders/?search=Juan

Ejemplo POST pedido:

json
Copiar código
{
  "monto_total": "150.50",
  "estado": "pendiente",
  "cliente": 1
}
Ejemplo de respuesta:

json
Copiar código
{
  "id": 1,
  "fecha": "2025-10-15",
  "monto_total": "150.50",
  "estado": "pendiente",
  "cliente": 1,
  "cliente_detalle": {
    "id": 1,
    "nombre": "Juan Pérez",
    "direccion": "Av. Lima 123",
    "email": "juan@mail.com",
    "telefono": "999111222"
  },
  "cliente_nombre": "Juan Pérez"
}
🔍 Búsqueda
Buscar por nombre del cliente:
/api/orders/?search=Juan

Buscar por estado del pedido:
/api/orders/?search=pendiente

🧠 Funcionalidades evaluadas
Función	Endpoint	Puntos
Listar pedidos	/api/orders/	2
Crear pedido	/api/orders/	2
Editar pedido	/api/orders/{id}/	2
Eliminar pedido	/api/orders/{id}/	2
Buscar pedidos	/api/orders/?search=	2
CRUD clientes	/api/clients/	3
Relación pedido-cliente	JSON con cliente_detalle	3
Campo extra cliente_nombre	Personalizado	+1






 Autor:

Samir Haziel Alfonso Solorzano
TECSUP – Diseño y Desarrollo de Software
 Octubre 2025
GitHub: Hazielcode