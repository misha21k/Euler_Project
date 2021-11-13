"""
Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

a = 1
while True:
    b = a + 1
    while True:
        expression = a**2 + b**2 - (1000 - a - b)**2
        if expression >= 0:
            break
        b += 1
    if expression == 0:
        break
    a += 1

c = 1000 - a - b
print(a, b, c)
print(a*b*c)
