total = 0

for n in range(2, 1000):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        total += n

print("Sum =", total)
