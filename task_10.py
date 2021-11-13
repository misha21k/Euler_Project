"""
Summation of primes
The sum of the primes below 10 is 2 + 3 + 7 = 17
Find the sum of all the primes below two million
"""

prime_numbers = {}
sum = 2
next = 3
last_number = int(input('Enter range of numbers (last number): '))
while next < last_number:
    if next in prime_numbers:
        number = prime_numbers.pop(next)
        composite_number = next + 2*number
        while composite_number in prime_numbers:
            composite_number += 2*number
        prime_numbers[composite_number] = number
    else:
        prime_numbers[next**2] = next
        sum += next
    next += 2

print(sum)