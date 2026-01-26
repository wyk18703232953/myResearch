from math import gcd

def func(l, r):
    if l == 1:
        l += 1
    if r - l < 2:
        return -1

    if l & 1:
        if r - l > 2:
            l += 1
            return '{} {} {}'.format(l, l + 1, l + 2)

        else:
            if gcd(l, l + 2) != 1:
                return '{} {} {}'.format(l, l + 1, l + 2)
            return -1
    return '{} {} {}'.format(l, l + 1, l + 2)


def main(n):
    l = 1
    r = max(3, n + 2)
    result = func(l, r)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)