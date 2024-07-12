from flask import Flask, jsonify , request 
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route("/cursos", methods= ["GET"]) 
def mostrar_cursos(): 
    db = mysql.connector.connect(
        user = "root",
        password = "0809",
        database = "capacitaciones"
    )
    
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cursos2024")
    
    cursos = cursor.fetchall()
    cursor.close()
    return jsonify(cursos)
    
@app.route("/quitar_curso/<int:id>", methods= ["DELETE"]) 
def quitar_cursos(id):
    
    db = mysql.connector.connect(
        user = "root",
        password = "0809",
        database = "capacitaciones"
    )
    
    cursor = db.cursor()
    cursor.execute("DELETE FROM cursos2024 where id = %s",(id,))
    db.commit() 
    cursor.close()
    return jsonify({"mensaje":"EL CURSO YA FUE QUITADO"})

@app.route("/agregar_cursos", methods= ["POST"]) 
def agregar_cursos():
    info = request.json
    db = mysql.connector.connect(
        user = "root",
        password = "0809",
        database = "capacitaciones"
    )
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO cursos2024 (nombre, dictado_por, fecha, precio) VALUES (%s,%s,%s,%s )", (info["nombre"],info["dictado_por"],info["fecha"],info["precio"]))
    db.commit() 
    cursor.close()
    return jsonify({"mensaje":"NUEVO OFERTA DE CURSO AGREGADA EXITOSAMENTE"})

@app.route("/actualizar_cursos/<int:id>", methods= ["PUT"]) 
def actualizar_cursos(id):
    info = request.json
    db = mysql.connector.connect(
        user = "root",
        password = "0809",
        database = "capacitaciones"
    )
    
    cursor = db.cursor()
    cursor.execute("UPDATE cursos2024 SET nombre= %s, dictado_por= %s, fecha= %s, precio= %s WHERE id= %s", (info["nombre"],info["dictado_por"],info["fecha"],info["precio"],id))
    db.commit() 
    cursor.close()
    return jsonify({"mensaje":"ACTUALIZADO EXITOSAMENTE"})


if __name__== "__main__":
    app.run(debug=True)

