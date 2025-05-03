from flask import Flask, render_template, request, redirect
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
    cursor.execute("SELECT id, nombre, fecha_nacimiento, matricula, correo, carrera FROM Estudiantes")
    estudiantes = cursor.fetchall()
    cnxn.close()

    return render_template('index.html', estudiantes=estudiantes)

@app.route('/delete/<int:id>', methods=["POST"])
def delete(id): 
    cnxn = get_connection()
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM Estudiantes WHERE id = ?", (id,))  
    cnxn.commit()
    cnxn.close()

    return redirect('/') 

@app.route('/edit/<int:id>', methods=["GET"])  
def edit(id):
    cnxn = get_connection()
    cursor = cnxn.cursor()
    cursor.execute("SELECT id, nombre, fecha_nacimiento, matricula, correo, carrera FROM Estudiantes WHERE id = ?", (id,))  # Corregido: se agregó coma
    estudiante = cursor.fetchone()
    cnxn.close()
    
    return render_template('update.html', estudiante=estudiante)

@app.route('/update/<int:id>', methods=["POST"])
def update(id):
    nombre = request.form['myName']
    fecha_nacimiento = request.form['myDate']
    matricula = request.form['myMatr']
    correo = request.form['myEmail']
    carrera = request.form['myCareer']
    
    cnxn = get_connection()
    cursor = cnxn.cursor()
    cursor.execute("UPDATE Estudiantes SET nombre = ?, fecha_nacimiento = ?, matricula = ?, correo = ?, carrera = ? WHERE id = ?", 
                  (nombre, fecha_nacimiento, matricula, correo, carrera, id))
    cnxn.commit()
    cnxn.close()
    
    return redirect('/')

@app.route('/insert', methods=["GET"])  
def show_insert_form():
    return render_template('insert.html')

@app.route('/insert', methods=["POST"])  
def insert():
    nombre = request.form['myName']
    fecha_nacimiento = request.form['myDate']
    matricula = request.form['myMatr']
    correo = request.form['myEmail']
    carrera = request.form['myCareer']
        
    cnxn = get_connection()
    cursor = cnxn.cursor()
    
    cursor.execute("INSERT INTO Estudiantes (nombre, fecha_nacimiento, matricula, correo, carrera) VALUES (?, ?, ?, ?, ?)", 
                  (nombre, fecha_nacimiento, matricula, correo, carrera))
    cnxn.commit()
    cnxn.close()

    return redirect('/') 

if __name__ == '__main__':
    app.run(debug=True)