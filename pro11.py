a = 5
c = 3
m = 16

x = int(input("Enter Seed: "))
n = int(input("How many numbers: "))

for i in range(n):
    x = (a * x + c) % m
    print(x)
