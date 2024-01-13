import json
import base64
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Descifrado

#Datos del ejercicio:
clave_etiqueta = "cifrado-sim-aes-256"
iv_hex = "00000000000000000000000000000000"
texto_cifrado_base64 = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="
clave_keystore = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"
#Pasamos nuestra clave y el IV a bytes:
clave_keystore_bytes = bytes.fromhex(clave_keystore)
iv_desc_bytes = bytes.fromhex(iv_hex)

#Decodificamos el texto cifrado en Base64:
texto_cifrado = base64.b64decode(texto_cifrado_base64)

#El Cifrado:
cipher = AES.new(clave_keystore_bytes, AES.MODE_CBC, iv_desc_bytes)
#Desciframos:
mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado), AES.block_size, style="x923")

print(mensaje_des_bytes.hex())
print(b64encode(mensaje_des_bytes).decode('utf-8'))
print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))