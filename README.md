# API de Biblioteca - Backend

Este proyecto es una API desarrollada con **Django** y **Django REST Framework** para gestionar información de libros, autores y más. A continuación, encontrarás las instrucciones paso a paso para levantar el servidor backend en tu máquina local.

## Requisitos previos

Antes de iniciar, asegúrate de tener instalado lo siguiente:

- [Python 3.x](https://www.python.org/downloads/) (versión 3.7 o superior recomendada)
- [Git](https://git-scm.com/)
- [pip](https://pip.pypa.io/en/stable/installation/) (instalado junto con Python)
- Un entorno virtual (opcional pero recomendado) como `venv` o `virtualenv`.

## Instalación

Sigue los siguientes pasos para configurar y ejecutar el servidor de forma local:

### 1. Clonar el repositorio

Clona este repositorio usando el comando Git:

```bash
git clone https://github.com/tu_usuario/nombre-del-repositorio.git
```

### 2. Crear y activar un entorno virtual

Es recomendable utilizar un entorno virtual para aislar las dependencias del proyecto.

#### Para sistemas Unix/macOS:

```bash
cd nombre-del-repositorio
python3 -m venv env
source env/bin/activate
```

#### Para sistemas Windows:

```bash
cd nombre-del-repositorio
python -m venv env
env\Scripts\activate
```

### 3. Instalar las dependencias

Una vez que el entorno virtual esté activo, instala las dependencias del proyecto utilizando el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Es posible que necesites configurar algunas variables de entorno. Un ejemplo básico de configuración en el archivo .env (si estás utilizando django-environ u otro paquete similar):

```bash
SECRET_KEY='tu_secreto'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5. Aplicar las migraciones

Para configurar la base de datos del proyecto, necesitas aplicar las migraciones. Las migraciones son archivos que Django usa para sincronizar los modelos de tu aplicación con la base de datos.

Primero, ejecuta el siguiente comando para crear las migraciones necesarias:

```bash
python manage.py makemigrations
```

Luego, aplica las migraciones a la base de datos con el siguiente comando:

```bash
python manage.py migrate
```

### 6. Crear un superusuario

Para acceder al panel de administración de Django y gestionar los datos de la aplicación, necesitas crear un superusuario. 

Ejecuta el siguiente comando para iniciar el proceso de creación del superusuario:

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor de desarrollo

Finalmente, levanta el servidor de desarrollo local con el siguiente comando:

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/` por defecto.

## Documentación de la API

Puedes acceder a la documentación generada automáticamente por **djangorestframework** en la siguiente URL:

```
http://127.0.0.1:8000/docs/
```

### Uso

Una vez que el servidor esté en funcionamiento, podrás realizar solicitudes HTTP a las diferentes rutas de la API usando una herramienta como Postman o cURL.

### Contribuciones

Si deseas contribuir a este proyecto, por favor, sigue los siguientes pasos:

    Haz un fork del proyecto.
    1. Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
    2.  Realiza tus cambios y haz commit (git commit -m 'Añadir nueva característica').
    3. Empuja tus cambios a la rama (git push origin feature/nueva-caracteristica).
    4. Abre un Pull Request.

### Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE en este repositorio.
