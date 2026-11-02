p = 23
g = 5

a = int(input("Enter Private Key of A: "))
b = int(input("Enter Private Key of B: "))

A = (g ** a) % p
B = (g ** b) % p

print("Public Key A:", A)
print("Public Key B:", B)

keyA = (B ** a) % p
keyB = (A ** b) % p

print("Shared Key at A:", keyA)
print("Shared Key at B:", keyB)
