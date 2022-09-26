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
class SerVoluntario(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from voluntario""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _nombres = request.form['nombres']
            _apellidos = request.form['apellidos']
            _dni = request.form['dni']
            _fecha_n = request.form['fecha_n']
            _celular = request.form['celular']
            _actividad = request.form['actividad']
            insert_user_cmd = """INSERT INTO voluntario(nombres, apellidos, dni, fecha_n, celular, actividad) 
                                VALUES(%s, %s, %s, %s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_nombres, _apellidos, _dni, _fecha_n, _celular, _actividad))
            conn.commit()
            response = jsonify(message='Voluntario inscrito exitosamente.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Falló añadir el voluntario.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)


#Get a user by id, update or delete user
class Voluntario(Resource):
    def get(self, v_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('select * from voluntario where id = %s',v_id)
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def put(self, v_id):
        try:
            var = 0
            conn = mysql.connect()
            cursor = conn.cursor()
            _aceptado = request.form['aceptado']
            if _aceptado == 'SI': var = 1
            update_user_cmd = """update voluntario 
                                 set aceptado=%s
                                 where id=%s"""
            cursor.execute(update_user_cmd, (var, v_id))
            conn.commit()
            response = jsonify('Voluntario actualizado exitosamente.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Falló en actualizar el voluntario.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

    def delete(self, v_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('delete from voluntario where id = %s', v_id)
            conn.commit()
            response = jsonify('Voluntario eliminado exitosamente.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Falló en eliminar el voluntario.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

#API resource routes
api.add_resource(SerVoluntario, '/servoluntarios', endpoint='servoluntarios')
api.add_resource(Voluntario, '/voluntario/<int:v_id>', endpoint='voluntario')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=False)