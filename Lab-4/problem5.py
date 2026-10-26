N = int(input("Enter N: "))

a = 0
b = 1

while a < N:
    print(a)
    a, b = b, a + b
