import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Clave y nonce proporcionados
clave = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
nonce = b64decode('9Yccn/f5nJJh')

# Texto a cifrar
texto_plano = 'He descubierto el error y no volveré a hacerlo mal'

# Cifrado
datos_asociados_bytes = bytes("felipe,profesor de keepcoding", "UTF-8")
cipher = AES.new(clave, AES.MODE_GCM, nonce=nonce)

# Esto es importante hacerlo en orden.
cipher.update(datos_asociados_bytes)

# Vamos a cifrar y autenticar.
texto_cifrado_bytes, tag = cipher.encrypt_and_digest(pad(texto_plano.encode('utf-8'), AES.block_size))

# Presentación en hexadecimal y base64
print("Texto cifrado en hexadecimal: " + texto_cifrado_bytes.hex())
print("Tag en hexadecimal: " + tag.hex())
print("Texto cifrado en base64: " + b64encode(texto_cifrado_bytes).decode('utf-8'))
print("Tag en base64: " + b64encode(tag).decode('utf-8'))