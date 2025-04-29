""" Nombre del proyecto: Sistema de Registro de Estudiantes

Descripción: Este proyecto consiste en desarrollar una aplicación que permita registrar, consultar, actualizar y eliminar información de estudiantes. Cada estudiante tendrá datos básicos como nombre completo, fecha de nacimiento, matrícula, correo electrónico y carrera. Toda la información será almacenada en una base de datos relacional (por ejemplo, MySQL, PostgreSQL o SQL Server). El sistema debe garantizar la integridad de los datos, ofrecer una interfaz sencilla (tipo consola o web básica) y permitir búsquedas por diferentes criterios (por matrícula, nombre, etc.). También se incluirá validación de datos al momento de registrar o actualizar estudiantes.

Objetivos principales:P
- Crear la estructura de la base de datos (tablas, relaciones, restricciones).
- Desarrollar la lógica para operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
- Implementar una interfaz amigable para interactuar con el sistema.
- Asegurar que los datos se validen correctamente antes de ser almacenados."""

from flask import Flask, render_template_string
import pyodbc

app = Flask(__name__)

# Función para conectarse a la base de datos
def get_connection():
    return pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-EK6KQLL\MSSQLSERVER_2022;'
        r'DATABASE=Students;'
        r'Trusted_Connection=yes;'
    )

# Ruta principal para mostrar los estudiantes
@app.route('/')
def mostrar_estudiantes():
    cnxn = get_connection()
    cursor = cnxn.cursor()
    cursor.execute("SELECT nombre, fecha_nacimiento, matricula, correo, carrera FROM Estudiantes")
    estudiantes = cursor.fetchall()
    cnxn.close()

    # Plantilla HTML básica
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Registro de Estudiantes</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            table { border-collapse: collapse; width: 80%; margin: auto; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
            th { background-color: #4CAF50; color: white; }
            tr:nth-child(even) { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h2 style="text-align:center;">Lista de Estudiantes</h2>
        <table>
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Fecha de Nacimiento</th>
                    <th>Matrícula</th>
                    <th>Correo</th>
                    <th>Carrera</th>
                </tr>
            </thead>
            <tbody>
                {% for estudiante in estudiantes %}
                <tr>
                    <td>{{ estudiante[0] }}</td>
                    <td>{{ estudiante[1] }}</td>
                    <td>{{ estudiante[2] }}</td>
                    <td>{{ estudiante[3] }}</td>
                    <td>{{ estudiante[4] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    '''
    return render_template_string(html, estudiantes=estudiantes)

if __name__ == '__main__':
    app.run(debug=True)

