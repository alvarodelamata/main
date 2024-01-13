from Crypto.Hash import HMAC, SHA256

key=bytes.fromhex("A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB")
mensaje_bytes = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.","utf8")
hmac256 = HMAC.new(key,mensaje_bytes,digestmod=SHA256)

#Representamos el valor:
print(hmac256.hexdigest())