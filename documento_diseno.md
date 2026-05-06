# Diseño del Sistema de Tickets

## Sobre mí
**Nombre:** Andres Felipe Charry Camacho
**Perfil:** Estudiante de último año de Ingeniería de Sistemas y Computación. Cuento con experiencia en el desarrollo de servicios backend y validación de datos clínicos en el  Programa Madre Canguro y consultoría técnica funcional en Avisini Software. Tengo un fuerte enfoque en el uso de Python y SQL para construir sistemas escalables y optimizados. 

---

## Decisiones Técnicas
Elegí **Django** porque es súper rápido para montar este tipo de sistemas. Usé la arquitectura que trae por defecto (MVT) y manejé todo con **plantillas HTML y Bootstrap**, así el código es fácil de leer y no se necesita un front separado.

### Portabilidad y Despliegue
Para asegurar que el proyecto funcione en cualquier entorno sin conflictos de dependencias, incluí soporte para **Docker** y **Docker Compose**. 

Además, siguiendo las mejores prácticas que aplico en mi experiencia profesional actual (Programa Madre Canguro), implementé una orquestación de comandos mediante `package.json`. Esto permite usar comandos estandarizados como `npm run docker:local` para levantar el ambiente de pruebas de forma consistente entre todos los miembros del equipo, y facilita el despligue en un entorno de producción.

### Enfoque en UX/UI
Aunque el sistema es sencillo, se puso especial cuidado en la interfaz para que fuera profesional y moderna:
*   **Tipografía:** Uso de 'Inter' vía Google Fonts para una lectura más clara y estética.
*   **Iconografía:** Integración de FontAwesome para dar contexto visual a las acciones y botones.
*   **Diseño Limpio:** Uso de sombras suaves, bordes redondeados y una paleta de colores coherente para una experiencia de usuario superior.

### Categorías de los Tickets
Se definieron tres categorías fundamentales: **Soporte Técnico**, **Facturación** y **Sugerencia**.
*   **Justificación:** Estas categorías cubren el espectro básico de necesidades de cualquier usuario. **Soporte** atiende fallos operativos, **Facturación** gestiona dudas administrativas y **Sugerencia** permite recolectar feedback. Este criterio garantiza una clasificación inicial clara que facilita el trabajo del administrador.

### Valor Agregado: Registro de Usuarios
Aunque el requerimiento inicial mencionaba que no era necesario, se decidió implementar un sistema de **Registro de Usuarios** con validación y encriptación de contraseñas. Esto se hizo para demostrar dominio sobre el flujo completo de autenticación y seguridad en Django, y para facilitar las pruebas a los evaluadores sin depender únicamente de usuarios pre-creados.

---

## Modelos de Datos
El sistema se basa en tres tablas principales:
1.  **User:** El sistema de usuarios que ya trae Django.
2.  **Categoria:** Para clasificar los problemas.
3.  **Ticket:** Donde guardamos el título, descripción, el estado y la respuesta del admin.

### Diagrama de Clases
![Clases](docs/diagrama_clases.png)

### Diagrama Entidad-Relación
![Base de Datos](docs/diagrama_er.png)

---

## Notas y Asunciones
*   Decidí usar **SQLite** para que puedan probar el proyecto de una sin configurar servidores de base de datos pesados.
*   Por seguridad, el estado del ticket solo se puede cambiar desde el Panel de Admin de Django.
*   Los usuarios solo ven sus propios tickets, puse filtros en las vistas para asegurar esto.
*   **Seguridad de Contraseñas:** Se implementó un sistema de registro que utiliza el hashing de contraseñas nativo de Django (algoritmo PBKDF2 con SHA256), garantizando que las contraseñas nunca se guarden en texto plano.

---

## Uso de IA
Para este proyecto usé **Antigravity (un asistente de IA)**. Me ayudó principalmente a generar la estructura base de los archivos, y  redactar la documentación técnica para ir más rápido.
