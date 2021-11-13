n = 600851475143
a = 2
while a ** 2 < n:
    while n % a == 0:
        n = n // a
    a += 1
print(n)
