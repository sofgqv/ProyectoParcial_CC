from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

#Create an instance of Flask
app = Flask(__name__)

#Create an instance of MySQL
mysql = MySQL()

#Create an instance of Flask RESTful API
api = Api(app)
#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'utec'
app.config['MYSQL_DATABASE_DB'] = 'llevame_pe' #nombre base de datos
app.config['MYSQL_DATABASE_HOST'] = '3.230.38.83'
app.config['MYSQL_DATABASE_PORT'] = 8005

#Initialize the MySQL extension
mysql.init_app(app)

#Get All Users, or Create a new user
class Donar(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from donacion""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

class Donaciones(Resource):
    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _nombres = request.form['nombres']
            _apellidos = request.form['apellidos']
            _dni = request.form['dni']
            _correo = request.form['correo']
            _monto = request.form['monto']
            insert_user_cmd = """INSERT INTO donacion(nombres, apellidos, dni, correo, monto) 
                                VALUES(%s, %s, %s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_nombres, _apellidos, _dni, _correo, _monto))
            conn.commit()
            response = jsonify(message='Donación inscrita exitosamente.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Falló añadir la donación.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)     

#API resource routes
api.add_resource(Donar, '/donar', endpoint='donar')
api.add_resource(Donaciones, '/donaciones', endpoint='donaciones')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002, debug=False)