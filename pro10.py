from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key = RSA.generate(2048)
msg = input("Enter Message: ")
hash = SHA256.new(msg.encode())
signature = pkcs1_15.new(key).sign(hash)
print("Signature Generated")

try:
    pkcs1_15.new(key.publickey()).verify(hash, signature)
    print("Signature Verified")
except:
    print("Verification Failed")
