
import json
"""
from hashlib import pbkdf2_hmac
import os

def generate_salt():
    salt = os.urandom(16)
    return salt.hex()

def generate_hash(plain_password, password_salt):
    password_hash = pbkdf2_hmac(
        "sha256",
        b"%b" % bytes(plain_password, "utf-8"),
        b"%b" % bytes(password_salt, "utf-8"),
        10000,
    )
    return password_hash.hex()

email = 'admin@llevame.com.pe'
password = '#ClaveSecreta123'
password_salt = generate_salt()
password_hash = generate_hash(password, password_salt)
print(password_salt)
print(password_hash)
"""

x = [["{'dni': '72182282', 'celular': '981325831', 'fecha_n': '2004-04-23', 'nombres': 'Valeria Nicole', 'actividad': 'embajadores', 'apellidos': 'Espinoza Tarazona'}"], ["{'dni': '75210256', 'celular': '949715915', 'fecha_n': '2004-03-03', 'nombres': 'Sof\u00eda Valeria', 'actividad': 'redes sociales', 'apellidos': 'Garc\u00eda Quintana'}"], ["{'dni': '18011030', 'celular': '997926162', 'fecha_n': '1966-06-06', 'nombres': 'Miguel Ignacio', 'actividad': 'entrega de donaciones', 'apellidos': 'de las Casas Diezcanseco'}"], ["{'dni': '72182282', 'celular': '981325831', 'fecha_n': '2004-04-23', 'nombres': 'Valeria Nicole', 'actividad': 'embajadores', 'apellidos': 'Espinoza Tarazona'}"], ["{'dni': '75210256', 'celular': '949715915', 'fecha_n': '2004-03-03', 'nombres': 'Sof\u00eda Valeria', 'actividad': 'redes sociales', 'apellidos': 'Garc\u00eda Quintana'}"], ["{'dni': '18011030', 'celular': '997926162', 'fecha_n': '1966-06-06', 'nombres': 'Miguel Ignacio', 'actividad': 'entrega de donaciones', 'apellidos': 'de las Casas Diezcanseco'}"]]