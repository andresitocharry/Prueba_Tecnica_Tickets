# Sistema Básico de Tickets - Prueba Técnica

Este es un sistema sencillo de gestión de tickets desarrollado en Django para una prueba técnica. Permite a los usuarios autenticados crear tickets de soporte, listar sus propios tickets y ver el detalle de los mismos. El administrador puede gestionar los tickets desde el panel administrativo.

## Requisitos Previos

- Python 3.9 o superior.
- Pip (gestor de paquetes de Python).

## Instalación y Configuración

Siga estos pasos para configurar el proyecto localmente:

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repo>
   cd PruebaTecnica_Tickets
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realizar migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Cargar datos de prueba (Categorías y Usuarios):**
   ```bash
   python manage.py loaddata initial_data.json
   ```

6. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

El sistema estará disponible en `http://127.0.0.1:8000/`.

---

## Credenciales de Prueba

Para facilitar la revisión, se han incluido los siguientes usuarios:

### Administrador (Acceso a /admin/)
- **Usuario:** `admin`
- **Contraseña:** `admin123`

### Usuario Estándar (Acceso a la plataforma de tickets)
- **Usuario:** `usuario_test`
- **Contraseña:** `password123`

---

## Funcionalidades Implementadas

- **Autenticación:** Inicio de sesión, cierre de sesión y registro de nuevos usuarios con encriptación de contraseñas.
- **Gestión de Tickets:** Crear, listar y ver detalle de tickets propios.
- **Panel Administrativo:** Gestión de categorías, cambio de estados de tickets y registro de respuestas administrativas.
- **Seguridad:** Los usuarios solo pueden ver y acceder a los tickets que ellos mismos han creado. Hashing de contraseñas mediante PBKDF2/SHA256.
