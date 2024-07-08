# MinicoreDjango-React

Erick Rosero 
7/7/2024

usuario de django: admin / Admin
contraseña: Admin1234!

https://github.com/KireLord/MinicoreDjango-React
 
link del frontend: https://github.com/KireLord/tareas-frontend

Este proyecto es una aplicación de gestión de tareas desarrollada utilizando Django para el backend y React para el frontend. Permite a los usuarios seleccionar un rango de fechas para ver las tareas que están en progreso y han pasado su fecha estimada de finalización.

## Tecnologías Utilizadas

- **Backend**: Django
- **Frontend**: React
- **Base de Datos**: SQLite (por defecto en Django)
- **HTTP Cliente**: Axios

## Características

- Visualización de tareas en progreso que han pasado su fecha estimada de finalización.
- Selección de rango de fechas para filtrar las tareas.
- Interfaz de usuario responsiva y moderna.

## Instalación y Configuración

### Backend (Django)

1. **Clonar el repositorio**:

    ```bash
    git clone https://github.com/tu-usuario/gestion-de-tareas.git
    cd gestion-de-tareas
    ```

2. **Crear un entorno virtual e instalar las dependencias**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Aplicar las migraciones y crear un superusuario**:

    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

4. **Correr el servidor de desarrollo**:

    ```bash
    python manage.py runserver
    ```

### Frontend (React)

1. **Navegar al directorio del frontend**:

    ```bash
    cd tareas-frontend
    ```

2. **Instalar las dependencias**:

    ```bash
    npm install
    ```

3. **Correr el servidor de desarrollo de React**:

    ```bash
    npm start
    ```

### Configuración de CORS

Para permitir que el frontend de React se comunique con el backend de Django, es necesario configurar CORS en Django.

1. **Instalar django-cors-headers**:

    ```bash
    pip install django-cors-headers
    ```

2. **Agregar `corsheaders` a `INSTALLED_APPS` y configurar los middleware en `settings.py`**:

    ```python
    INSTALLED_APPS = [
        ...
        'corsheaders',
        ...
    ]

    MIDDLEWARE = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        ...
    ]

    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
    ]
    ```

## Estructura del Proyecto

### Backend (Django)

- `models.py`: Define los modelos `Empleado`, `Proyecto` y `Tarea`.
- `serializers.py`: Define el serializador `TareaPasadaSerializer`.
- `views.py`: Contiene la vista `tareas_pasadas_view` para filtrar y devolver las tareas en progreso y pasadas de fecha.
- `urls.py`: Define la ruta para la vista `tareas_pasadas_view`.

### Frontend (React)

- `src/TareasList.js`: Componente principal que muestra el formulario para seleccionar fechas y la tabla de tareas.
- `src/App.js`: Componente principal de la aplicación.
- `src/index.css`: Estilos globales para la aplicación.

## Uso

1. **Iniciar el backend y el frontend** como se describe en la sección de instalación y configuración.
2. **Acceder a la aplicación** en `http://localhost:3000`.
3. **Seleccionar un rango de fechas** y hacer clic en "Buscar Tareas" para ver las tareas en progreso y pasadas de fecha.


