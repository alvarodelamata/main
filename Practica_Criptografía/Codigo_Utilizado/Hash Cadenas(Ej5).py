import hashlib

m = hashlib.sha3_224()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","utf8"))
print("sha3 - 224:    " + m.digest().hex())

m = hashlib.sha3_256()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","utf8"))
print("sha3 - 256:    " + m.digest().hex())

m = hashlib.md5()
m.update(bytes("Hola", "utf8"))
print("md5:    " + m.digest().hex())

m = hashlib.sha1() 
m.update(bytes("Hola", "utf8"))
print("SHA1:   " + m.digest().hex())

m = hashlib.sha256()  #SHA2
m.update(bytes("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72", "utf8"))
print("SHA256 resultado: " + m.digest().hex())


m = hashlib.sha256()  #SHA2
m.update(bytes("Holo", "utf8"))
print("SHA256 Holo: " + m.digest().hex()) # Propiedad de difusión y efecto avalancha. NO SE PARECE UN HUEVO A UNA CASTAÑA.

m = hashlib.sha3_256()
m.update(bytes("Hola","utf8"))
print("sha3 - 256:    " + m.digest().hex())

m = hashlib.sha512()
m.update(bytes("Hola", "utf8"))
print("SHA512: " + m.digest().hex())
print(m.digest_size)