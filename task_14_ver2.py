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

def count_chain(n):
    global values
    try:
        return values[n]
    except KeyError:
        if n % 2 == 0:
            values[n] = 1 + count_chain(n // 2)
        else:
            values[n] = 2 + count_chain((3*n + 1)//2)
    return values[n]

longest_chain = 0
answer = -1
values = {1: 1}

for number in range(500000, 1000000):
    chain = count_chain(number)
    if chain > longest_chain:
        longest_chain = chain
        answer = number

print(answer)