"""
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
What is the 10001st prime numbers?
"""

# version 1
prime_numbers = []
count = 0
number = 2
last = 50000000
next1000 = {i for i in range(number, last + 1)}
while number <= last:
    if number in next1000:
        prime_numbers.append(number)
        count += 1
        # if count == 10001:
        #     break
        item = number**2
        while item <= last:
            next1000.discard(item)
            item += number
    number += 1

print(count, prime_numbers[-1])