import random
import hashlib


#generate the prime number
def prime_generator(bits):
    while True:
        prime = random.getrandbits(bits)
        prime |= (1 << (bits - 1)) | 1

        if is_prime(prime):
            return prime

#Checks if the number is prime
def is_prime(n, k=40):
    """ Miller-Rabin' test"""
    if n == 2 or n == 3:
        return True

    if n < 2 or n % 2 == 0:
        return False

    r, s = 0, n - 1

    while s % 2 == 0:
        r += 1
        s //= 2

    for i in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)

        if x == 1 or x == n - 1:
            continue

        for i in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

#generates the pair of keys
def key_pair():
    p = prime_generator(1024)
    q = prime_generator(1024)
    phi_n = (p - 1) * (q - 1)
    n = p * q
    e = 65537
    d = pow(e, -1, phi_n)

    return (n, e), (n, d)

#padding
def padding(message, k):
    hash_len = hashlib.sha256().digest_size
    message_len = len(message)

    if message_len > k - 2 * hash_len - 2:
        raise ValueError('Message  size out of range')

    padded_message = b'\x00' * (k - message_len - 2 * hash_len - 2) + b'\x01' + message
    random_string = bytes(random.randint(0, 255) for _ in range(hash_len))
    masked_message = hashlib.sha256(random_string + padded_message).digest() + padded_message
    masked_padded_message = random_string + masked_message

    return masked_padded_message

#upaded the message
def unpadding(masked_random_string, k):
    hash_len = hashlib.sha256().digest_size

    if len(masked_random_string) != k:
        raise ValueError("Cyphered text out of range")

    masked_message = masked_random_string[hash_len:]
    padded_message = masked_message[hash_len:]
    start_index = padded_message.find(b'\x01')

    if start_index == -1:
        raise ValueError("Unable to unpad.")

    original_message = padded_message[start_index + 1:]

    return original_message

def encrypt(message, public_key):
    n, e = public_key
    message_bytes = message.encode()
    k = (n.bit_length() + 7) // 8
    masked_random_string = padding(message_bytes, k)
    m = int.from_bytes(masked_random_string, 'big')
    ciphertext = pow(m, e, n)

    return ciphertext


def decrypt(ciphertext, private_key):
    n, d = private_key
    m = pow(ciphertext, d, n)
    k = (n.bit_length() + 7) // 8
    masked_random_string = m.to_bytes(k, 'big')
    recovered_message_bytes = unpadding(masked_random_string, k)
    recovered_message = recovered_message_bytes.decode()

    return recovered_message








