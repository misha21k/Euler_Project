"""
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
What is the 10001st prime numbers?
"""

# version 2
prime_numbers = {}
count = 0
max_prime = 0
next = 1
n = int(input('Enter number of prime number, what you want to find: '))
while count < n:
    next += 1
    if next in prime_numbers:
        for number in prime_numbers.pop(next):
            if next + number in prime_numbers:
                prime_numbers[next + number].add(number)
            else:
                prime_numbers[next + number] = {number}
    else:
        prime_numbers[next**2] = {next}
        max_prime = next
        count += 1

print('{0}th prime number is {1}'.format(n, max_prime))
