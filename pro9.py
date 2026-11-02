from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public = key.publickey()
cipher = PKCS1_OAEP.new(public)
text = input("Enter Message: ")
encrypted = cipher.encrypt(text.encode())
print("Encrypted:", encrypted.hex())
decrypt = PKCS1_OAEP.new(key)
plain = decrypt.decrypt(encrypted)
print("Decrypted:", plain.decode())
