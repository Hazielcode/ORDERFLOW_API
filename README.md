🧩 ORDERFLOW_API

API REST creada con Django + Django REST Framework para administrar clientes y pedidos.
Cada pedido pertenece a un cliente, y todas las operaciones se hacen mediante endpoints del API (sin usar el panel admin de Django).
El sistema permite crear, listar, actualizar, eliminar y buscar registros fácilmente.

⚙️ Tecnologías utilizadas

Python 3.12

Django 5.1.2

Django REST Framework 3.15.2

django-filter 24.3

SQLite (base de datos por defecto)

🚀 Cómo ejecutar el proyecto

Clonar el repositorio:

git clone https://github.com/Hazielcode/ORDERFLOW_API.git
cd ORDERFLOW_API


Crear entorno virtual e instalar dependencias:

py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt


Aplicar migraciones y ejecutar el servidor:

python manage.py migrate
python manage.py runserver


El servidor estará disponible en:
👉 http://127.0.0.1:8000/api/

📚 Endpoints disponibles
👤 CLIENTES (/api/clients/)
Método	Descripción	Ejemplo
GET	Listar todos los clientes	curl http://127.0.0.1:8000/api/clients/
POST	Crear nuevo cliente	curl -X POST -H "Content-Type: application/json" -d "{\"nombre\":\"Juan Pérez\",\"direccion\":\"Av. Lima 123\",\"email\":\"juan@mail.com\",\"telefono\":\"999111222\"}" http://127.0.0.1:8000/api/clients/
PUT/PATCH	Editar cliente	curl -X PATCH -H "Content-Type: application/json" -d "{\"direccion\":\"Av. Arequipa 999\"}" http://127.0.0.1:8000/api/clients/1/
DELETE	Eliminar cliente	curl -X DELETE http://127.0.0.1:8000/api/clients/1/

Ejemplo POST cliente:

{
  "nombre": "Juan Pérez",
  "direccion": "Av. Lima 123",
  "email": "juan@mail.com",
  "telefono": "999111222"
}

📦 PEDIDOS (/api/orders/)
Método	Descripción	Ejemplo
GET	Listar todos los pedidos	curl http://127.0.0.1:8000/api/orders/
POST	Crear nuevo pedido	curl -X POST -H "Content-Type: application/json" -d "{\"monto_total\":\"150.50\",\"estado\":\"pendiente\",\"cliente\":1}" http://127.0.0.1:8000/api/orders/
PUT/PATCH	Editar pedido	curl -X PATCH -H "Content-Type: application/json" -d "{\"estado\":\"enviado\"}" http://127.0.0.1:8000/api/orders/1/
DELETE	Eliminar pedido	curl -X DELETE http://127.0.0.1:8000/api/orders/1/
GET (search)	Buscar por nombre o estado	/api/orders/?search=Juan o /api/orders/?search=pendiente

Ejemplo POST pedido:

{
  "monto_total": "150.50",
  "estado": "pendiente",
  "cliente": 1
}


Ejemplo de respuesta JSON:

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

Se puede buscar pedidos por nombre de cliente o estado:

curl http://127.0.0.1:8000/api/orders/?search=Juan
curl http://127.0.0.1:8000/api/orders/?search=pendiente

👨‍💻 Autor

Samir Haziel Alfonso Solorzano
TECSUP – Diseño y Desarrollo de Software
📅 Octubre 2025
🐙 GitHub: Hazielcode

🟢 Proyecto probado y funcionando al 100% con Postman.