
max = 0
for i in range(999, 99, -1):
    if max > i**2:
        break
    for j in range(i, 99, -1):
        product = i*j
        if product > max and str(product) == str(product)[::-1]:
            max = product
print(max)

