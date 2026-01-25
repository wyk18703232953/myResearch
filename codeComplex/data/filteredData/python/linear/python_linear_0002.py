from math import floor
import re

z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert_num(x):
    output = ""
    row, col = [int(x) for x in re.split("(\d+)", x) if x.isnumeric()]
    while col > 0:
        y = (col - 1) % 26
        output += z[y]
        col = floor((col - 1) / 26)
    return f"{output[::-1]}{row}"

def convert_alpha(x):
    output = 0
    word = ("".join([i for i in x if i.isalpha()]))[::-1]
    for i in range(0, len(word)):
        output += (z.index(word[i]) + 1) * 26 ** i
    ending = x[len(word):]
    return f"R{ending}C{output}"

def generate_input_string(idx):
    if idx % 2 == 0:
        word_len = idx % 5 + 1
        row = idx + 1
        letters = "".join(z[(idx + j) % 26] for j in range(word_len))
        return f"{letters}{row}"
    else:
        row = idx + 1
        col = idx * 3 + 1
        return f"R{row}C{col}"

def main(n):
    output = ""
    for i in range(n):
        hehexd = generate_input_string(i)
        if hehexd.startswith("R") and len(hehexd) > 1 and hehexd[1].isnumeric() and "C" in hehexd:
            output += f"{convert_num(hehexd)}\n"
        else:
            output += f"{convert_alpha(hehexd)}\n"
    print(output, end="")

if __name__ == "__main__":
    main(10)