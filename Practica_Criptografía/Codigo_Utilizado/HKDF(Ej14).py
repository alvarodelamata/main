from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets
from Crypto.Random import get_random_bytes

#elemento_diversificacion = secrets.token_bytes(16)
elemento_diversificacion = bytes.fromhex("34323536373231323335343132333435")

#salt = get_random_bytes(16)
#master_secret = secrets.token_bytes(64)
master_secret = bytes.fromhex("79b126c9732fc7e9c5faca8c0f5c3e1681b4c1d9c183085dc9061f2dc83eedf2")



key1 = HKDF(master_secret, 32, elemento_diversificacion, SHA512, 1)

print("Clave key1: ", key1.hex())
