# Sistema de Tickets de Soporte (Django)

Este proyecto es una solución robusta y profesional para la gestión de tickets de soporte, desarrollada como parte de una prueba técnica.

---

## 🚀 Demo en Vivo
Puede probar la aplicación desplegada en tiempo real en el siguiente enlace:
**[https://prueba-tecnica-tickets.onrender.com/](https://prueba-tecnica-tickets.onrender.com/)**

---

## 🛠️ Tecnologías Utilizadas
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

## Ejecución con Docker (Ambiente Local Estandarizado)

Siguiendo buenas prácticas de desarrollo para garantizar un ambiente local consistente (metodología aplicada en entornos profesionales como el **Programa Madre Canguro**), se ha incluido un orquestador de comandos mediante `npm`.

Si tiene Docker y Node.js instalados, puede levantar el proyecto con:

```bash
npm run docker:local
```

O si prefiere usar Docker directamente:

```bash
docker-compose up --build
```

Este comando:
1. Construye la imagen de Python.
2. Realiza las migraciones automáticamente.
3. Carga los datos de prueba (`initial_data.json`).
4. Inicia el servidor en el puerto 8000.

---

## Ejecución de Tests

Para verificar la integridad del sistema y las reglas de seguridad (privacidad de tickets y acceso), ejecute el siguiente comando:

```bash
python manage.py test tickets
```

---

## Calidad de Código (Linting)

Para asegurar que el código cumple con los estándares **PEP8**, puede ejecutar el linter:

```bash
# Usando npm
npm run lint

# O directamente con flake8
flake8 .
```

---

## Interfaz y Diseño

Se ha implementado una interfaz moderna utilizando:
- **Bootstrap 5** con personalización de estilos CSS.
- **FontAwesome** para iconografía.
- **Google Fonts (Inter)** para mejorar la legibilidad.
- Diseño responsivo compatible con dispositivos móviles.

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
