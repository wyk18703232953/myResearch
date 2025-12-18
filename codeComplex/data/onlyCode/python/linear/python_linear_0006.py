import re
import string
import math

letter_number_pattern = "[a-zA-Z]*[0-9]*"

alpha = dict(zip(range(1,28), string.ascii_uppercase))
decimals = dict(zip(string.ascii_uppercase, range(1,27)))


alpha_len = len(alpha)

def letter_to_decimal(n):
    exponents = []
    pow_i = 0
    while True:
        if n // (26**pow_i) > 26:
            exponents.append(1)
            n = n - (26**pow_i)
            pow_i += 1
        else:
            exponents.append(n // (26**pow_i))
            n = n - ((n // (26**pow_i)) * (26**pow_i))
            break
    pow_i = pow_i - 1
    while n != 0:
        t = n // (26**pow_i)
        n = n - (t * (26 ** pow_i))
        exponents[pow_i] = exponents[pow_i] + t
        pow_i = pow_i - 1
    result = ''.join(list(map(lambda x: alpha[x], reversed(exponents))))
    return result


def letters_to_deci(letters):
    total_sum = 0
    pows = list(reversed(range(len(letters))))
    for i in range(len(letters)):
        total_sum += decimals[letters[i]] * (26**pows[i])
    return total_sum

input_cells = []

n_lines = input()
for i in range(int(n_lines)):
    input_cells.append(input())

for cell in input_cells:
    all_matches = re.findall(letter_number_pattern, cell)[:-1]
    if len(all_matches) == 2:
        rows = int(re.search("[0-9]*$", all_matches[0]).group())
        cols = int(re.search("[0-9]*$", all_matches[1]).group())
        converted_cols = letter_to_decimal(cols)
        print("%s%s" % (converted_cols, rows))
    elif len(all_matches) == 1:
        rows = re.match("[A-Z]*", all_matches[0]).group()
        cols = re.search("[0-9]*$", all_matches[0]).group()
        converted_rows = letters_to_deci(rows)
        print("R%sC%s" % (cols, converted_rows))
    else:
        pass