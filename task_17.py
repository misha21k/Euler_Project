"""
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.
If all the number from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces ar hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

UNITS = {1: 'one',
         2: 'two',
         3: 'three',
         4: 'four',
         5: 'five',
         6: 'six',
         7: 'seven',
         8: 'eight',
         9: 'nine',
         10: 'ten',
         11: 'eleven',
         12: 'twelve',
         13: 'thirteen',
         14: 'fourteen',
         15: 'fifteen',
         16: 'sixteen',
         17: 'seventeen',
         18: 'eighteen',
         19: 'nineteen'}

TENS = {2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'}

HUNDREDS = {i: '{}hundred'.format(UNITS[i]) for i in range(1, 10)}

sum = 0
for number in range(1, 1000):
    line = ''
    div, mod = divmod(number, 100)
    if div:
        line = HUNDREDS[div]
        if mod:
            line += 'and'
    if 1 <= mod <= 19:
        line += UNITS[mod]
    elif mod > 19:
        div, mod = divmod(mod, 10)
        line += TENS[div]
        if mod:
            line += UNITS[mod]
    sum += len(line)
line = 'onethousand'
sum += len(line)
print(sum)
