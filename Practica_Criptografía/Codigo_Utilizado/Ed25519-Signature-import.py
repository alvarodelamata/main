import ed25519


privatekey = open("ed25519-priv","rb").read()

signedKey = ed25519.SigningKey(privatekey)
msg = bytes('Firmamos esto con la curva 25519','utf8')
signature = signedKey.sign(msg, encoding='hex')

print("Firma Generada (64 bytes):", signature)


