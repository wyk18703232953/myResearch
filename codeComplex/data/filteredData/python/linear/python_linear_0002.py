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

def generate_input_list(n):
    res = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            # generate RC form: R{row}C{col}
            row = i
            col = i * 3
            res.append(f"R{row}C{col}")

        else:
            # generate letters+number form
            num = i * 2
            # deterministic letter pattern based on i
            # map i to one or two letters
            first = z[(i - 1) % 26]
            second = z[(i // 26) % 26] if i > 26 else ""
            letters = first + second
            res.append(f"{letters}{num}")
    return res

def main(n):
    inputs = generate_input_list(n)
    output = ""
    for hehexd in inputs:
        if hehexd.startswith("R") and len(hehexd) > 2 and hehexd[1].isnumeric() and "C" in hehexd:
            output += f"{convert_num(hehexd)}\n"

        else:
            output += f"{convert_alpha(hehexd)}\n"
    return output

if __name__ == "__main__":
    # example deterministic call
    # print(main(10))
    pass