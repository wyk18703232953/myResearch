def main(n):
    if n % 4 == 2:
        return -1

    def oracle(x):
        return (x * x + n) % (n // 2 + 3)

    a = oracle(1)
    b = oracle(1 + n // 2)

    if a == b:
        return 1

    l = 1
    r = 1 + n // 2

    while l != r:
        mid = (l + r) // 2
        c = oracle(mid)
        d = oracle(mid + n // 2)

        if c == d:
            return mid

        if a < b:
            if c < d:
                l = mid + 1

            else:
                r = mid

        else:
            if c > d:
                l = mid + 1

            else:
                r = mid

    return l


if __name__ == "__main__":
    # example deterministic calls
    for size in [4, 8, 16, 32]:
        res = main(size)
        # print(size, res)
        pass