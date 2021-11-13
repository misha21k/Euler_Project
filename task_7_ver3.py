"""
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
What is the 10001st prime numbers?
"""

# version 3
composite_and_prime = {}  # key is composite number, value is prime
count = 1  # we count found prime number
max_prime = 2  # maximum prime number, which we find
next = 1  # next number, which we check
n = int(input('Enter number of prime number, what you want to find: '))
while count < n:
    next += 2  # we check only odd number
    if next in composite_and_prime:  # next is composite number
        prime = composite_and_prime.pop(next)
        composite = next + 2 * prime  # we seek new composite number for prime
        while composite in composite_and_prime:
            composite += 2 * prime
        composite_and_prime[composite] = prime
    else:  # next is prime number
        composite_and_prime[next ** 2] = next
        max_prime = next
        count += 1
        # if count % 100000 == 0:
        #     print('{0}th prime number is {1}'.format(count, max_prime))
        # if max_prime >= 2147483647:
        #     print('{0}th prime number is {1}'.format(count, max_prime))
        #     break

print('{0}th prime number is {1}'.format(n, max_prime))
