# 🚀 ORDERFLOW_API
### Sistema de Gestión de Pedidos y Clientes — *Django + Django REST Framework*

![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.1.2-success?logo=django)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.15.2-red?logo=django)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Status](https://img.shields.io/badge/status-Finalizado-brightgreen)

---

## 🧠 Descripción General

**ORDERFLOW_API** es una API REST creada con **Django + Django REST Framework**, que permite administrar **Pedidos** (Entidad 1) y **Clientes** (Entidad 2).  
Cada pedido pertenece a un cliente, y el sistema ofrece un CRUD completo, búsqueda, filtros y respuesta personalizada.

📦 **Entidad 1 → Pedidos:** contiene `fecha`, `monto_total`, `estado`, y relación con cliente.  
👤 **Entidad 2 → Clientes:** contiene `nombre`, `dirección`, `email`, y `teléfono`.

✅ Todo el CRUD se implementa vía **endpoints DRF**, sin usar el panel de administración de Django.

---

## ⚙️ Tecnologías Usadas

| Tecnología | Versión | Descripción |
|-------------|----------|--------------|
| 🐍 Python | 3.12 | Lenguaje base |
| 🟢 Django | 5.1.2 | Framework backend |
| 🔴 Django REST Framework | 3.15.2 | Creación de API REST |
| 🧩 django-filter | 24.3 | Filtros y búsqueda |
| 💾 SQLite | Default | Base de datos local |

---

## 🧱 Instalación y Ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/Hazielcode/ORDERFLOW_API.git
cd ORDERFLOW_API
2️⃣ Crear entorno virtual e instalar dependencias
bash
Copiar código
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
3️⃣ Migrar base de datos y ejecutar servidor
bash
Copiar código
python manage.py migrate
python manage.py runserver
La API estará disponible en 👉 http://127.0.0.1:8000/api/

📚 Endpoints Principales
🧍 Clientes (/api/clients/)
Método	Endpoint	Descripción
GET	/api/clients/	Listar todos los clientes
POST	/api/clients/	Crear nuevo cliente
PUT	/api/clients/{id}/	Actualizar cliente
PATCH	/api/clients/{id}/	Actualizar parcialmente cliente
DELETE	/api/clients/{id}/	Eliminar cliente

📦 Ejemplo POST Cliente:

json
Copiar código
{
  "nombre": "Juan Pérez",
  "direccion": "Av. Lima 123",
  "email": "juan@mail.com",
  "telefono": "999111222"
}
📦 Pedidos (/api/orders/)
Método	Endpoint	Descripción
GET	/api/orders/	Listar todos los pedidos
POST	/api/orders/	Crear pedido
PUT	/api/orders/{id}/	Actualizar pedido
PATCH	/api/orders/{id}/	Actualizar parcialmente pedido
DELETE	/api/orders/{id}/	Eliminar pedido
GET	/api/orders/?search=Juan	Buscar por cliente
GET	/api/orders/?search=pendiente	Buscar por estado

📦 Ejemplo POST Pedido:

json
Copiar código
{
  "monto_total": "150.50",
  "estado": "pendiente",
  "cliente": 1
}
✅ Respuesta esperada:

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
🔍 Búsqueda y Filtros
Se puede buscar por nombre de cliente o estado del pedido:

bash
Copiar código
GET /api/orders/?search=Juan
GET /api/orders/?search=pendiente
🧠 Evaluación Oficial (Rubrica)
Funcionalidad	Descripción	Puntos
GET /orders/	Listado general	2
POST /orders/	Crear pedido	2
PUT/PATCH /orders/{id}/	Editar pedido	2
DELETE /orders/{id}/	Eliminar pedido	2
GET /orders/?search=	Búsqueda por filtro	2
GET /clients/	CRUD Clientes	3
Relación Pedido-Cliente	Mostrar info asociada	3
Campo cliente_nombre personalizado	Extra opcional	+1
TOTAL		17/16 pts 🎯

🧩 Estructura del Proyecto
markdown
Copiar código
orderflow_api/
├─ manage.py
├─ orderflow_api/
│  ├─ settings.py
│  ├─ urls.py
│  └─ asgi.py / wsgi.py
└─ orders/
   ├─ models.py
   ├─ serializers.py
   ├─ views.py
   ├─ migrations/
   └─ __init__.py
🧪 Pruebas (Postman)
1️⃣ Crear cliente
2️⃣ Listar clientes
3️⃣ Crear pedido
4️⃣ Listar pedidos
5️⃣ Editar pedido (PUT)
6️⃣ Buscar por cliente (?search=Juan)
7️⃣ Eliminar pedido
8️⃣ Eliminar cliente

💡 Campo extra: todas las respuestas de pedidos incluyen:

json
Copiar código
"cliente_nombre": "Juan Pérez"
🧾 Versión y Cambios
Versión	Descripción
v1.0.0	Versión inicial del proyecto
v1.1.0	Serializers y búsqueda avanzada
v1.2.0	Documentación completa (README y comentarios)

📹 Video (YouTube)
🎬 En el video se debe mostrar:

Ejecución del servidor (python manage.py runserver)

Pruebas en Postman (crear, listar, buscar, editar y eliminar)

Relación entre pedido y cliente en JSON

Campo cliente_nombre (+1 punto)

Confirmación final de funcionalidad completa

👨‍💻 Autor
Samir Haziel Alfonso Solorzano
🎓 Estudiante de Diseño y Desarrollo de Software - TECSUP
📍 Lima, Perú
📅 Octubre 2025
🐙 GitHub: Hazielcode
📧 Email: haziel.dev@gmail.com

⭐ “Software limpio, simple y funcional.”
Proyecto ORDERFLOW_API — Evaluación final Django REST Framework 2025-2