def substraction(a, b):
    if a == 0 or b == 0:
        return 0

    else:
        if a > b:
            count = a // b
            return substraction(a % b, b) + count

        else:
            count = b // a
            return substraction(a, b % a) + count


def main(n):
    t = max(1, n)
    res = []
    for i in range(t):
        a = i + 1
        b = 2 * i + 3
        res.append(substraction(a, b))
    for val in res:
        # print(val)
        pass
if __name__ == "__main__":
    main(5)