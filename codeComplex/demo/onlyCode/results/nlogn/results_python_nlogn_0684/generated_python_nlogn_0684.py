def main(n):
    m = n
    a = sorted(range(1, n + 1))
    s = sorted(range(2, 2 * n + 2, 2))
    if a[-1] > s[0]:
        return -1
    else:
        if a[-1] == s[0]:
            return sum(a[:-1]) * m + sum(s)
        else:
            return sum(a[:-2]) * m + a[-2] * (m - 1) + sum(s) + a[-1]


if __name__ == "__main__":
    print(main(5))