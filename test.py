def next_prime(prime, prime_numbers):
    while True:
        prime += 2
        if prime in prime_numbers:
            number = prime_numbers.pop(prime)
            composite_number = prime + 2*number
            while composite_number in prime_numbers:
                composite_number += 2*number
            prime_numbers[composite_number] = number
        else:
            prime_numbers[prime**2] = prime
            yield prime, prime_numbers


for prime, prime_numbers in next_prime(1, {}):
    print(prime)
    if prime > 100:
        break
