import hashlib

def hash(message):
    hash = hashlib.sha3_256()
    hash.update(message)
    hash = hash.digest()

    return hash

def sign(message, private_key):
    hashing = hash(message)
    hash_to_number = int.from_bytes(hashing, 'big')
    signature = pow(hash_to_number, private_key[1], private_key[0])

    return signature

def check(message, siganature, public_key):
    hashed = hash(message)
    number_to_hash = int.from_bytes(hashed, 'big')
    decipher_signature = pow(siganature, public_key[1], public_key[0])

    return decipher_signature == number_to_hash