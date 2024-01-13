import hashlib
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


#Cifrado
textoPlano_bytes = bytes.fromhex('00000000000000000000000000000000')

clave = bytes.fromhex('A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72')
iv_bytes = bytes.fromhex('00000000000000000000000000000000')
cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)
texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='pkcs7'))
print("KCV AES:", texto_cifrado_bytes.hex()[0:6])
print("texto_cifrado con padding: ", texto_cifrado_bytes.hex())

#cipher2 = AES.new(clave, AES.MODE_CBC,iv_bytes)
#texto_cifrado_bytes = cipher2.encrypt(textoPlano_bytes)
#print("KCV AES:", texto_cifrado_bytes.hex()[0:6])
#print("texto_cifrado sin padding: ", texto_cifrado_bytes.hex())

m = hashlib.sha256()
m.update(bytes.fromhex("f946108299307d3f6f7585b96013346d"))
print("KCV SHA256: " + m.digest().hex()[0:6])