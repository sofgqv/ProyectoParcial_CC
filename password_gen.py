
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