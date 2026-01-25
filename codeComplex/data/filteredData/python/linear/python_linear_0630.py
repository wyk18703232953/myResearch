from math import ceil


def solve(n, k):
    if k == 1:
        return n - 1
    if k == 2:
        if n > 1:
            return n - 1
        else:
            return -1
    if k == 3:
        if n > 2:
            return n - 1
        else:
            return -1
    if k in {4, 5}:
        if n > 1:
            return n - 2
        else:
            return -1

    if 2 * n + 1 <= len(bin(3 * k)[2:]):
        return -1
    else:
        return n - ceil((len(bin(3 * k)[2:]) - 1) / 2)


def main(n):
    t = n
    for i in range(1, t + 1):
        ni = i + 1
        ki = (i % 7) + 1
        a = solve(ni, ki)
        if a == -1:
            print('NO')
        else:
            print('YES', a)


if __name__ == "__main__":
    main(10)