# RSA Algorithm - Encryption & Decryption

# Function to find GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):

    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


# -------- USER INPUT --------
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

# Step 1: Calculate n
n = p * q

# Step 2: Calculate phi
phi = (p - 1) * (q - 1)

print("\nValue of n:", n)
print("Value of phi:", phi)

# Step 3: Choose e
e = int(input("Enter public key e (1 < e < phi and gcd(e,phi)=1): "))

if gcd(e, phi) != 1:
    print("e and phi are not coprime. Restart program.")
    exit()

# Step 4: Find private key d
d = mod_inverse(e, phi)

print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# -------- Encryption --------
message = int(input("\nEnter numeric message to encrypt: "))

cipher = pow(message, e, n)
print("Encrypted Message:", cipher)

# -------- Decryption --------
decrypted = pow(cipher, d, n)
print("Decrypted Message:", decrypted)