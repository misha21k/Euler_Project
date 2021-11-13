"""
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million
"""

length_for_numbers = {1: 1}
max_length = 1
max_number = 1
for number in range(1, 1000000):
    n = number
    sequence = []
    while n not in length_for_numbers:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    length = len(sequence) + length_for_numbers[n]
    if length > max_length:
        max_length = length
        max_number = number
    for i in range(1, len(sequence) + 1):
        length_for_numbers[sequence[-i]] = i + length_for_numbers[n]

print(max_number)
