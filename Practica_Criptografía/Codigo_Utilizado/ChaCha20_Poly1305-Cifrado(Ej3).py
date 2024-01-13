from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode

textoPlano_bytes = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
#El nonce que se ha proporcionado en base_64 y yo lo he pasado con un conversor online a hex (9Yccn/f5nJJhAt2S -> f5871c9ff7f99c926102dd92)
nonce_mensaje = bytes.fromhex('f5871c9ff7f99c926102dd92')
print('nonce  = ', nonce_mensaje.hex())

#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
texto_cifrado_bytes = cipher.encrypt(textoPlano_bytes)
print('Mensaje cifrado en HEX = ', texto_cifrado_bytes.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado_bytes).decode())

