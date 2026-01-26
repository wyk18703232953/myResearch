import argparse

def is_golden(total, integers):
    current_total = 0
    for i, val in enumerate(integers):
        current_total += val
        if current_total < total:
            continue
        elif current_total == total:
            splice = integers[i+1:]
            return (not splice) or is_golden(total, splice)
        elif current_total > total:
            return False
    return False

def main(n):
    # n 作为票据长度，生成确定性的数字串 "1234567890123..."
    if n <= 0:
        # print("YES")
        pass
        return

    digits = []
    for i in range(n):
        d = (i % 10) + 1
        if d == 10:
            d = 0
        digits.append(str(d))
    ticket = "".join(digits)

    integers = [int(x) for x in ticket]

    zeros = 0
    while zeros < len(integers) and integers[-1*(zeros+1)] == 0:
        zeros += 1

    if zeros > 0 and zeros >= len(integers):
        integers = []
    elif zeros > 0:
        integers = integers[:-1*zeros]

    if not integers:
        # print("YES")
        pass
        return
    if len(integers) == 1:
        # print("NO")
        pass
        return

    total = 0
    for i, val in enumerate(integers[:-1]):
        total += val
        splice = integers[i+1:]
        if is_golden(total, splice):
            # print("YES")
            pass
            return
    # print("NO")
    pass
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=10)
    args = parser.parse_args()
    main(args.n)