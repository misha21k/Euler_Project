"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

n = 20
# Will find simple factors of numbers from 2 to n and maximum number each of them
simple_factors = {}  # key - simple factors, value - maximum number of key
for i in range(2, n+1):
    current = i  # current number from 2 to n
    factor = 2  # first possible simple factor
    while factor <= current:
        count = 0
        while current % factor == 0:  # If factor is factor of current,
            count += 1  # we count its number. Factor can be only simple
            current //= factor
        try:  # If factor is in simple_factors and its number more number in simple_factors,
            simple_factors[factor] = max(simple_factors[factor], count)  # we change its number
        except KeyError:  # If factor is not in simple_factors,
            simple_factors[factor] = count  # we add it
        factor += 1  # next factor. It can be not simple

# We find minimum number, which divided by numbers from 2 to n
resul = 1
for factor, number in simple_factors.items():
    resul *= factor**number
print(resul)
