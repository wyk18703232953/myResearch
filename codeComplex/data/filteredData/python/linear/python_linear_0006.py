import re
import string
import math

letter_number_pattern = "[a-zA-Z]*[0-9]*"

alpha = dict(zip(range(1, 28), string.ascii_uppercase))
decimals = dict(zip(string.ascii_uppercase, range(1, 27)))

alpha_len = len(alpha)

def letter_to_decimal(n):
    exponents = []
    pow_i = 0
    while True:
        if n // (26 ** pow_i) > 26:
            exponents.append(1)
            n = n - (26 ** pow_i)
            pow_i += 1

        else:
            exponents.append(n // (26 ** pow_i))
            n = n - ((n // (26 ** pow_i)) * (26 ** pow_i))
            break
    pow_i = pow_i - 1
    while n != 0:
        t = n // (26 ** pow_i)
        n = n - (t * (26 ** pow_i))
        exponents[pow_i] = exponents[pow_i] + t
        pow_i = pow_i - 1
    result = ''.join(list(map(lambda x: alpha[x], reversed(exponents))))
    return result


def letters_to_deci(letters):
    total_sum = 0
    pows = list(reversed(range(len(letters))))
    for i in range(len(letters)):
        total_sum += decimals[letters[i]] * (26 ** pows[i])
    return total_sum


def generate_cell(index):
    # Even index: RC form like "R23C55"
    # Odd index: Excel-like form like "BC23"
    if index % 2 == 0:
        row = index + 1
        col = (index + 3) * 2
        return f"R{row}C{col}"

    else:
        # generate letters as Excel column title from index+1
        num = index + 1
        letters = []
        while num > 0:
            num -= 1
            letters.append(chr(ord('A') + (num % 26)))
            num //= 26
        letters = ''.join(reversed(letters))
        row = (index + 5) * 3
        return f"{letters}{row}"


def main(n):
    input_cells = [generate_cell(i) for i in range(n)]

    for cell in input_cells:
        all_matches = re.findall(letter_number_pattern, cell)[:-1]
        if len(all_matches) == 2:
            rows = int(re.search("[0-9]*$", all_matches[0]).group())
            cols = int(re.search("[0-9]*$", all_matches[1]).group())
            converted_cols = letter_to_decimal(cols)
            # print("%s%s" % (converted_cols, rows))
            pass
        elif len(all_matches) == 1:
            rows = re.match("[A-Z]*", all_matches[0]).group()
            cols = re.search("[0-9]*$", all_matches[0]).group()
            converted_rows = letters_to_deci(rows)
            # print("R%sC%s" % (cols, converted_rows))
            pass

        else:
            pass
if __name__ == "__main__":
    main(10)