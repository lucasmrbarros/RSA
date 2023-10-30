import random
import math

#Check if the number is a prime
def is_prime(number):
    if number < 2:
        return False
    for i in range (2, number // 2+1):
        if number % 1 == 0:
            return False
    return True

#generates the prime number
def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse (e, phi):
    for d in range (3, phi):
        if(d * e) % phi == 1:
            return d

p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)

#check if both of the primes aren't the same
while p == q:
    q = generate_prime(1000, 5000)

n = p * q
phi_n = (p - 1) * (q -1)

e = random.randint(3, phi_n-1)

while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n -1)

d = mod_inverse(e, phi_n)

print("Public key: ", e)
print("Private key: ", d)
print("N: ", n)
print("Phi: ", phi_n)
print("P: ", p)
print("Q: ", )

message = "Hello World"

message_encoded = [ord(c) for c in message]

ciphertext = [pow(c, e, n) for c in message_encoded]

print(ciphertext)

message_encoded = [pow(ch, d, n) for ch in ciphertext]
message = "".join("")