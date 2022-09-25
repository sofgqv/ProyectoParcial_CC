from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
import jwt
import os
from hashlib import pbkdf2_hmac

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

def generate_jwt_token(content):
    token = jwt.encode(content, "secret", algorithm="HS256")
    return token


def generate_hash(plain_password, password_salt):
    password_hash = pbkdf2_hmac(
        "sha256",
        b"%b" % bytes(plain_password, "utf-8"),
        b"%b" % bytes(password_salt, "utf-8"),
        10000,
    )
    return password_hash.hex()

def db_read(query, params=None):
    conn = mysql.connect()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    entries = cursor.fetchall()[0]
    cursor.close()
    content = []

    for entry in entries:
        content.append(entry)
    
    return content

def validate_user(email, password):
    current_user = db_read("""SELECT * FROM users WHERE email = %s""", (email,))

    if current_user:
        saved_password_salt = current_user[2]
        saved_password_hash = current_user[3]
        password_hash = generate_hash(password, saved_password_salt)
        
        if password_hash == saved_password_hash:
            user_id = current_user[0]
            jwt_token = generate_jwt_token({"id": user_id})
            return jwt_token
        else:
            return False
    else:
        return False

class Admin(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('select * from users')
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    
    def post(self):
        try:
            user_email = request.form["email"]
            user_password = request.form["password"]
            user_token = validate_user(user_email, user_password)
            
            if user_token:
                response = jsonify({"jwt_token": user_token})
                response.status_code = 200
            else:
                response = jsonify('Usuario o contraseña inválidos.')
                response.status_code = 401
        except Exception as e:
            print(e)
            response = jsonify('Falló utilizar el login.')         
            response.status_code = 400
        finally: 
            return(response)

class CheckToken(Resource):
    def post(self):
        try:
            jwt_token = request.form["token"]
            body = jwt.decode(jwt_token, "secret", algorithms=["HS256"])
            if body:
                response = jsonify('Se inició la sesión correctamente.')
                response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Falló el inicio de sesión.')         
            response.status_code = 400
        finally: 
            return(response)

api.add_resource(Admin, '/admin', endpoint='admin')
api.add_resource(CheckToken, '/token', endpoint='token')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8004, debug=False)