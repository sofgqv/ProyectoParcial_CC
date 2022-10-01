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
class Adoptar(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select id, nombres, apellidos, dni, DATE_FORMAT(fecha_n, "%Y-%m-%d") as fecha_n, celular, correo, mascota_id, aceptado from adoptar""")
            rows = cursor.fetchall()
            lista = collections.OrderedDict()
            for row in rows:
                dictionary = collections.OrderedDict()
                dictionary['id'] = row[0]
                dictionary['nombres'] = row[1]
                dictionary['apellidos'] = row[2]
                dictionary['dni'] = row[3]
                dictionary['fecha_n'] = row[4]
                dictionary['celular'] = row[5]
                dictionary['correo'] = row[6]
                dictionary['mascota_id'] = row[7]
                dictionary['aceptado'] = row[8]
                lista[row[0]] = dictionary
            return jsonify(lista)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            body = request.get_json()
            _nombres = body.get('nombres', None)
            _apellidos = body.get('apellidos', None)
            _dni = body.get('dni', None)
            _fecha_n = body.get('fecha_n', None)
            _celular = body.get('celular', None)
            _correo = body.get('correo', None)
            _mascota_id = body.get('mascota_id', None)
            insert_user_cmd = """INSERT INTO adoptar(nombres, apellidos, dni, fecha_n, celular, correo, mascota_id) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_nombres, _apellidos, _dni, _fecha_n, _celular, _correo, _mascota_id))
            conn.commit()
            response = jsonify('Peticion de adopcion creada con exito.')
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


class AdoptarEstado(Resource):
    def patch(self, a_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            body = request.get_json()
            _aceptado = body.get('aceptado', None)
            update_user_cmd = """update adoptar 
                                 set aceptado=%s
                                 where id=%s"""
            cursor.execute(update_user_cmd, (_aceptado, a_id))
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
#Get a user by id, update or delete user

class Mascotas(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select id, nombre, raza, fecha_n, sexo, size, estado_adop from mascota""")
            rows = cursor.fetchall()
            lista = collections.OrderedDict()
            for row in rows:
                dictionary = collections.OrderedDict()
                dictionary['id'] = row[0]
                dictionary['nombre'] = row[1]
                dictionary['raza'] = row[2]
                dictionary['fecha_n'] = row[3]
                dictionary['sexo'] = row[4]
                dictionary['size'] = row[5]
                dictionary['estado_adop'] = row[6]
                lista[row[0]] = dictionary
            return jsonify(lista)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            
class MascotasAdd(Resource):
    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            body = request.get_json()
            _nombre = body.get('nombre', None)
            _raza = body.get('raza', None)
            _fecha_n = body.get('fecha_n', None)
            _sexo = body.get('sexo', None)
            _size = body.get('size', None)
            insert_user_cmd = """INSERT INTO mascota(nombre, raza, fecha_n, sexo, size) 
                                VALUES(%s, %s, %s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_nombre, _raza, _fecha_n, _sexo, _size))
            conn.commit()
            response = jsonify('Mascota creada con exito.')
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

class Mascota(Resource):
    def get(self, m_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select id, nombre, raza, fecha_n, sexo, size, estado_adop from mascota where id = %s""", m_id)
            row = cursor.fetchall()[0]
            dictionary = collections.OrderedDict()
            dictionary['id'] = row[0]
            dictionary['nombre'] = row[1]
            dictionary['raza'] = row[2]
            dictionary['fecha_n'] = row[3]
            dictionary['sexo'] = row[4]
            dictionary['size'] = row[5]
            dictionary['estado_adop'] = row[6]
            return jsonify(dictionary)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    def patch(self, m_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            body = request.get_json()
            _nombre = body.get('nombre', None)
            _raza = body.get('raza', None)
            _fecha_n = body.get('fecha_n', None)
            _sexo = body.get('sexo', None)
            _size = body.get('size', None)
            
            conn = mysql.connect()
            cursor = conn.cursor()
            body = request.get_json()
            _nombre = body.get('nombre', None)
            _raza = body.get('raza', None)
            _fecha_n = body.get('fecha_n', None)
            _sexo = body.get('sexo', None)
            _size = body.get('size', None)

            if (_nombre != ""):
                update_pet_cmd = """update mascota 
                                 set nombre=%s
                                 where id=%s"""
                cursor.execute(update_pet_cmd, (_nombre, m_id))

            if (_raza != ""): 
                update_pet_cmd = """update mascota 
                                 set raza=%s
                                 where id=%s"""
                cursor.execute(update_pet_cmd, (_raza, m_id))

            if (_fecha_n != ""):
                update_pet_cmd = """update mascota 
                                 set fecha_n=%s
                                 where id=%s"""
                cursor.execute(update_pet_cmd, (_fecha_n, m_id))

            if (_sexo != ""): 
                update_pet_cmd = """update mascota 
                                 set sexo=%s
                                 where id=%s"""
                cursor.execute(update_pet_cmd, (_sexo, m_id))

            if (_size != ""): 
                update_pet_cmd = """update mascota 
                                 set size=%s
                                 where id=%s"""
                cursor.execute(update_pet_cmd, (_size, m_id))
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
            cursor.execute("""delete from mascota where id = %s""", m_id)
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
api.add_resource(AdoptarEstado, '/adoptarestado/<int:a_id>', endpoint='adoptarestado')
api.add_resource(Adoptar, '/adoptar', endpoint='adoptar')
api.add_resource(Mascota, '/mascota/<int:m_id>', endpoint='mascota')
api.add_resource(Mascotas, '/mascotas', endpoint='mascotas')
api.add_resource(MascotasAdd, '/mascotasadd', endpoint='mascotasadd')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8003, debug=False)