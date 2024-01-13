from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

import os
my_path = os.path.abspath(os.getcwd())

fichero_pub = my_path + "\\clave-rsa-oaep-publ.pem"
f=open(fichero_pub,'r')
keypub= RSA.import_key(f.read())




mensaje = bytes.fromhex("e2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72")

encryptor = PKCS1_OAEP.new(keypub,SHA256)
encrypted = encryptor.encrypt(mensaje)

print("Cifrado:", encrypted.hex())
print("--------------------------------------------------")