DRF Simple CRUD
Este es un proyecto básico de API REST construido con Django REST Framework (DRF). Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una entidad Project.

📌 Características
Django 5.1.6 y Django REST Framework.
Base de datos configurable (SQLite por defecto, pero soporta PostgreSQL).
Despliegue en Render con configuración para producción.
Uso de WhiteNoise para manejo de archivos estáticos.
🚀 Instalación y Configuración
1️⃣ Clonar el repositorio
bash
Copy
Edit
git clone https://github.com/tu-usuario/drfsimplecrud.git
cd drfsimplecrud
2️⃣ Crear un entorno virtual
bash
Copy
Edit
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
3️⃣ Instalar dependencias
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Configurar la base de datos
El proyecto usa SQLite por defecto, pero si deseas cambiar a PostgreSQL, edita DATABASES en settings.py.

5️⃣ Aplicar migraciones y ejecutar el servidor
bash
Copy
Edit
python manage.py migrate
python manage.py runserver
La API estará disponible en http://127.0.0.1:8000/api/projects/.

🔥 Endpoints
Método	URL	Descripción
GET	/api/projects/	Listar proyectos
POST	/api/projects/	Crear un proyecto
GET	/api/projects/{id}/	Obtener un proyecto
PUT	/api/projects/{id}/	Actualizar un proyecto
DELETE	/api/projects/{id}/	Eliminar un proyecto
🛠 Tecnologías usadas
Django y Django REST Framework
PostgreSQL (opcional, puedes usar SQLite)
WhiteNoise para servir archivos estáticos
Render para despliegue en producció
