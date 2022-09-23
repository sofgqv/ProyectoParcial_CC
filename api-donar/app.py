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
app.config['MYSQL_DATABASE_DB'] = 'x' #nombre base de datos
app.config['MYSQL_DATABASE_HOST'] = '54.204.79.149'
app.config['MYSQL_DATABASE_PORT'] = 8005

#Initialize the MySQL extension
mysql.init_app(app)

#Get All Users, or Create a new user
class Donar(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from otg_demo_users""")
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
            _name = request.form['name']
            _age = request.form['age']
            _city = request.form['city']
            insert_user_cmd = """INSERT INTO otg_demo_users(name, age, city) 
                                VALUES(%s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_name, _age, _city))
            conn.commit()
            response = jsonify(message='User added successfully.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add user.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)       

#API resource routes
api.add_resource(Donar, '/donar', endpoint='donar')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002, debug=False)