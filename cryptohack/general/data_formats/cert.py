from Crypto.PublicKey import RSA

with open("2048b-rsa-example-cert.der", 'rb') as f:
    key = RSA.import_key(f.read())

print(key.n)
