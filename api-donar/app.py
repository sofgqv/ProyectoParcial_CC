import collections
from flask import Flask, jsonify, request
from flask_cors import CORS
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

CORS(app, resources={r'/*': {'origins': '*'}})

#Initialize the MySQL extension
mysql.init_app(app)

#Get All Users, or Create a new user
class Donaciones(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
<<<<<<< Updated upstream
            cursor.execute("""SELECT id, nombres, apellidos, dni, correo, monto FROM donacion""")
=======
            body = request.get_json()
            cursor.execute("""select id, nombres, apellidos, dni, correo, monto from donacion""")
>>>>>>> Stashed changes
            rows = cursor.fetchall()
            lista = collections.OrderedDict()
            for row in rows:
                dictionary = collections.OrderedDict()
                dictionary['id'] = row[0]
                dictionary['nombres'] = row[1]
                dictionary['apellidos'] = row[2]
                dictionary['dni'] = row[3]
                dictionary['correo'] = row[4]
                dictionary['monto'] = row[5]
                lista[row[0]] = dictionary
            return jsonify({"a" : 1})
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

class Donar(Resource):
    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            body = request.get_json()
            _nombres = body.get('nombres', None)
            _apellidos = body.get('apellidos', None)
            _dni = body.get('dni', None)
            _correo = body.get('correo', None)
            _monto = body.get('monto', None)
            insert_user_cmd = """INSERT INTO donacion(nombres, apellidos, dni, correo, monto) VALUES(%s, %s, %s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_nombres, _apellidos, _dni, _correo, _monto))
            conn.commit()
            response = jsonify(success=True, message='Donación inscrita exitosamente.', id=cursor.lastrowid, status_code=200)
            #response.data = cursor.lastrowid
        except Exception as e:
            print(e)
            response = jsonify(message = 'Falló añadir la donación.', status_code = 400)
        finally:
            cursor.close()
            conn.close()
            return(response)     

#API resource routes
api.add_resource(Donar, '/donar', endpoint='donar')
api.add_resource(Donaciones, '/donaciones', endpoint='donaciones')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002, debug=False)