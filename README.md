# Student_register

Aplicación web en Flask para registrar y administrar estudiantes (CRUD) sobre SQL Server.

## 1. Descripción

Sistema web que permite listar, agregar, editar y eliminar estudiantes. Usa **Flask** con plantillas Jinja2 y **Bootstrap**, y se conecta a SQL Server mediante **pyodbc**.

## 2. Características

- Lista de estudiantes en tabla (ID, nombre, fecha de nacimiento, matrícula, correo y carrera).
- Formulario para agregar estudiantes.
- Edición de los datos de un estudiante existente.
- Eliminación de estudiantes mediante petición `POST`.
- Consultas parametrizadas para evitar inyección SQL.

## 3. Tecnologías

- Python 3 · Flask
- SQL Server · pyodbc
- HTML · Bootstrap (plantillas Jinja2)

## 4. Requisitos

- Python 3.10 o superior
- SQL Server con una base de datos `Students` y la tabla `Estudiantes` (`id`, `nombre`, `fecha_nacimiento`, `matricula`, `correo`, `carrera`)
- ODBC Driver 17 for SQL Server

```bash
pip install flask pyodbc
```

## 5. Configuración

Edita la función `get_connection()` en `Student_register.py` con tu servidor y base de datos:

```python
r'SERVER=TU_SERVIDOR\TU_INSTANCIA;'
r'DATABASE=Students;'
r'Trusted_Connection=yes;'
```

## 6. Uso

```bash
python Student_register.py
```

Abre `http://127.0.0.1:5000` en el navegador.

| Ruta | Método | Función |
|------|--------|---------|
| `/` | GET | Lista de estudiantes |
| `/insert` | GET / POST | Formulario y creación |
| `/edit/<id>` | GET | Formulario de edición |
| `/update/<id>` | POST | Guarda los cambios |
| `/delete/<id>` | POST | Elimina el estudiante |

## 7. Estructura

```
Student_register/
├── Student_register.py
└── templates/
    ├── index.html     # Lista
    ├── insert.html    # Alta
    └── update.html    # Edición
```
