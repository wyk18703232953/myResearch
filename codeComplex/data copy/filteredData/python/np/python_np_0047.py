import math

def main(n):
    # n controls the length of the strings
    length = max(1, n)

    # deterministically construct inp and dec based on n
    # pattern for inp: cycle "+-"
    inp = "".join("+" if i % 2 == 0 else "-" for i in range(length))

    # pattern for dec:
    # first third: same as inp
    # second third: replace with '?'
    # last third: invert '+' and '-'
    third = max(1, length // 3)
    first_part = inp[:third]
    second_part = "?" * min(third, length - third)
    remaining = length - len(first_part) - len(second_part)
    last_source = inp[len(first_part) + len(second_part):len(first_part) + len(second_part) + remaining]
    last_part = "".join('+' if c == '-' else '-' for c in last_source)
    dec = (first_part + second_part + last_part)[:length]

    inp_dict = {"+": 0, "-": 0}
    dec_dict = {"+": 0, "-": 0, "?": 0}

    for ch in inp:
        if ch == "+":
            inp_dict["+"] += 1
        elif ch == "-":
            inp_dict["-"] += 1

    for ch in dec:
        if ch == "+":
            dec_dict["+"] += 1
        elif ch == "-":
            dec_dict["-"] += 1
        elif ch == "?":
            dec_dict["?"] += 1

    if dec_dict["+"] == inp_dict["+"] and dec_dict["-"] == inp_dict["-"]:
        print(1.0000000000)
    else:
        temp = inp_dict["+"] - dec_dict["+"]
        temp1 = inp_dict["-"] - dec_dict["-"]
        if temp + temp1 == dec_dict["?"] and temp >= 0 and temp1 >= 0:
            total = temp + temp1
            temp2 = math.factorial(total) / (math.factorial(temp) * math.factorial(temp1))
            for _ in range(total):
                temp2 *= 0.5
            print(temp2)
        else:
            print(0.0000000000)

if __name__ == "__main__":
    main(10)