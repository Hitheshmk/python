from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'12345678'
cipher = DES.new(key, DES.MODE_ECB)
text = input("Enter Text: ")
encrypted = cipher.encrypt(pad(text.encode(), 8))
print("Encrypted:", encrypted.hex())
decrypted = unpad(cipher.decrypt(encrypted), 8)
print("Decrypted:", decrypted.decode())
