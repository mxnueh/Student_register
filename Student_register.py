""" Nombre del proyecto: Sistema de Registro de Estudiantes

Descripción: Este proyecto consiste en desarrollar una aplicación que permita registrar, consultar, actualizar y eliminar información de estudiantes. Cada estudiante tendrá datos básicos como nombre completo, fecha de nacimiento, matrícula, correo electrónico y carrera. Toda la información será almacenada en una base de datos relacional (por ejemplo, MySQL, PostgreSQL o SQL Server). El sistema debe garantizar la integridad de los datos, ofrecer una interfaz sencilla (tipo consola o web básica) y permitir búsquedas por diferentes criterios (por matrícula, nombre, etc.). También se incluirá validación de datos al momento de registrar o actualizar estudiantes.

Objetivos principales:
- Crear la estructura de la base de datos (tablas, relaciones, restricciones).
- Desarrollar la lógica para operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
- Implementar una interfaz amigable para interactuar con el sistema.
- Asegurar que los datos se validen correctamente antes de ser almacenados."""

from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

def get_connection():
    return pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-EK6KQLL\MSSQLSERVER_2022;'
        r'DATABASE=Students;'
        r'Trusted_Connection=yes;'
    )

@app.route('/')
def mostrar_estudiantes():
    cnxn = get_connection()
    cursor = cnxn.cursor()
    cursor.execute("SELECT nombre, fecha_nacimiento, matricula, correo, carrera FROM Estudiantes")
    estudiantes = cursor.fetchall()
    cnxn.close()

    return render_template('index.html', estudiantes=estudiantes)

@app.route('/insert.html')
def insert():
    return render_template('insert.html')

if __name__ == '__main__':
    app.run(debug=True)

