def main(n):
    if n <= 0:
        return

    if n == 1:
        # print(1)
        pass
        return

    if n == 2:
        # print(1, 2)
        pass
        return

    if n == 3:
        # print(1, 1, 3)
        pass
        return

    ar = [0] * 30

    for i in range(30):
        ar[i] = n // (2 ** i) - n // (2 ** (i + 1))

    sd = 0
    out = []

    for i in range(30):
        if sd == n - 1:
            if n == (2 ** i):
                out.append(str(2 ** i))

            else:
                out.append(str(n - n % (2 ** (i - 1))))
            # print(" ".join(out))
            pass
            return
        for j in range(ar[i]):
            out.append(str(2 ** i))
            sd += 1
            if sd == n - 1:
                break

    # print(" ".join(out))
    pass
if __name__ == "__main__":
    main(10)