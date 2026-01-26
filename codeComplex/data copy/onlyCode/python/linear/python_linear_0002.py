from math import floor
import re

z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# numbers to row
# def convert_num(x):
#     output = ""
#     row, col = [int(x) for x in re.split("(\d+)", x) if x.isnumeric()]
#     while col > 0:
#         if col % 26 == 0:
#             col = floor(col / 26)
#             output += "Z"
#         else:
#             y = col % 26
#             output += z[y - 1]
#             col = floor(col / 26)
#     return f"{output[::-1]}{row}"
def convert_num(x):
    output = ""
    row, col = [int(x) for x in re.split("(\d+)", x) if x.isnumeric()]
    while col > 0:
        y = (col - 1) % 26
        output += z[y]
        col = floor((col - 1) / 26)
    return f"{output[::-1]}{row}"


# letters to alpha
def convert_alpha(x):
    output = 0
    word = ("".join([i for i in x if i.isalpha()]))[::-1]
    for i in range(0, len(word)):
        output += (z.index(word[i]) + 1) * 26 ** i
    ending = x[len(word) :]

    return f"R{ending}C{output}"


# print(convert_alpha("BC23"))
# print(convert_num("R23C55"))

i = int(input())
output = ""
for x in range(i):
    hehexd = input()
    if hehexd.startswith("R") and hehexd[1].isnumeric() and "C" in hehexd:
        output += f"{convert_num(hehexd)}\n"
    else:
        output += f"{convert_alpha(hehexd)}\n"
print(output)