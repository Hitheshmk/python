from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'0123456789abcdef'
cipher = AES.new(key, AES.MODE_ECB)
text = input("Enter Message: ")
encrypted = cipher.encrypt(pad(text.encode(), 16))
print("Encrypted:", encrypted.hex())
decrypted = unpad(cipher.decrypt(encrypted), 16)
print("Decrypted:", decrypted.decode())
