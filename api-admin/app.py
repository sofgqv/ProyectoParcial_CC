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

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

#Initialize the MySQL extension
mysql.init_app(app)

def generate_jwt_token(content):
    encoded_content = jwt.encode(content, JWT_SECRET_KEY, algorithm="HS256")
    token = str(encoded_content).split("'")[1]
    return token


def generate_hash(plain_password, password_salt):
    password_hash = pbkdf2_hmac(
        "sha256",
        b"%b" % bytes(plain_password, "utf-8"),
        b"%b" % bytes(password_salt, "utf-8"),
        10000,
    )
    return password_hash.hex()

def validate_user_input(input_type, **kwargs):
    if input_type == "authentication":
        if len(kwargs["email"]) <= 255 and len(kwargs["password"]) <= 255:
            return True
        else:
            return False

def validate_user(email, password):
    conn = mysql.connect()
    cursor = conn.cursor()
    current_user = cursor.execute("""SELECT * FROM users WHERE email = %s""", (email,))

    if len(current_user) == 1:
        saved_password_hash = current_user[0]["password_hash"]
        saved_password_salt = current_user[0]["password_salt"]
        password_hash = generate_hash(password, saved_password_salt)
        if password_hash == saved_password_hash:
            user_id = current_user[0]["id"]
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
            conn = mysql.connect()
            cursor = conn.cursor()
            user_email = request.form["email"]
            user_password = request.form["password"]

            user_token = validate_user(user_email, user_password)

            if user_token:
                response = jsonify({"jwt_token": user_token})
                response.status_code = 200
            else:
                response = jsonify('Usuario inválido.')
                response.status_code = 401
        except Exception as e:
            print(e)
            response = jsonify('Falló utilizar el login.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)

api.add_resource(Admin, '/admin', endpoint='admin')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8004, debug=False)