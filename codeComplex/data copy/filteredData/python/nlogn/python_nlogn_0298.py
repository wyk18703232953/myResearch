def main(n):
    # n controls both number of weights and length of operations
    # generate weights deterministically: w[i] = (value, index)
    # values are increasing to make sorted(reverse=True) meaningful
    w = [(i + 1, i + 1) for i in range(n)]

    # generate operation string k of length n
    # first n//2 operations are '0', remaining are '1'
    zeros = n // 2
    ones = n - zeros
    k = "0" * zeros + "1" * ones

    b = sorted(w, reverse=True)
    f = []
    p = []

    for ch in k:
        if ch == "0":
            if b:  # guard for cases when n is small
                x = b.pop()
                f.append(x)
                p.append(x[1])

        else:
            if f:
                y = f.pop()
                p.append(y[1])

    if p:
        # print(*p)
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)