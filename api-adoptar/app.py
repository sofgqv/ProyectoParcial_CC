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
app.config['MYSQL_DATABASE_HOST'] = '54.204.79.149'
app.config['MYSQL_DATABASE_PORT'] = 8005

#Initialize the MySQL extension
mysql.init_app(app)

#Get All Users, or Create a new user
class Adoptar(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from adoptar""")
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
            update_user_cmd = """update adoptar 
                                 set aceptado=%s
                                 where id=%s"""
            cursor.execute(update_user_cmd, (var, v_id))
            conn.commit()
            response = jsonify('Peticion de adopcion actualizada exitosamente.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Falló en actualizar la petción de adopción.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response) 


    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _nombres = request.form['nombres']
            _apellidos = request.form['apellidos']
            _dni = request.form['dni']
            _fecha_n = request.form['fecha_n']
            _celular = request.form['celular']
            _correo = request.form['correo']
            _mascota_id = request.form['mascota_id']
            insert_user_cmd = """INSERT INTO adoptar(nombres, apellidos, dni, fecha_n, celular, correo, mascota_id) 
                                VALUES(%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_nombres, _apellidos, _dni, _fecha_n, _celular, _correo, _mascota_id))
            conn.commit()
            response = jsonify(message='Peticion de adopcion creada con exito.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Falló la creación de la petición de adopción.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)
            
#Get a user by id, update or delete user

class Mascotas(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('select * from mascota')
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            
class Mascota(Resource):
    def get(self, m_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('select * from mascota where id = %s',m_id)
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
            _nombre = request.form['nombre']
            _raza = request.form['raza']
            _fecha_n = request.form['fecha_n']
            _sexo = request.form['sexo']
            _size = request.form['size']
            insert_user_cmd = """INSERT INTO mascota(nombre, raza, fecha_n, sexo, size) 
                                VALUES(%s, %s, %s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_nombre, _raza, _fecha_n, _sexo, _size))
            conn.commit()
            response = jsonify(message='Mascota creada con exito.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Falló la creación de la mascota.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)

    def put(self, m_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _nombre = request.form['nombre']
            _raza = request.form['raza']
            _fecha_n = request.form['fecha_n']
            _sexo = request.form['sexo']
            _size = request.form['size']
            update_pet_cmd = """update mascota 
                                 set nombre=%s, raza=%s, fecha_n=%s, sexo=%s, size=%s
                                 where id=%s"""
            cursor.execute(update_pet_cmd, (_nombre, _raza, _fecha_n, _sexo, _size, m_id))
            conn.commit()
            response = jsonify('Mascota actualizada exitosamente.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Falló la actualzación de la mascota.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

    def delete(self, m_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('delete from mascota where id = %s',m_id)
            conn.commit()
            response = jsonify('Mascota eliminada exitosamente.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Falló la eliminación de mascota.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

#API resource routes
api.add_resource(Adoptar, '/adoptar', endpoint='adoptar')
api.add_resource(Mascota, '/mascota/<int:m_id>', endpoint='mascota')
api.add_resource(Mascotas, '/mascotas', endpoint='mascotas')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8003, debug=False)