def main(n):
    # Deterministically generate input data based on n
    # a is a permutation of 0..n-1
    a = list(range(n))
    # b is a rotated version of a to keep logic meaningful and deterministic
    k = n // 2
    b = a[k:] + a[:k]

    ha = {}
    for i in range(n):
        ha[a[i]] = i
    removed = 0
    out = ""
    for i in range(n):
        if ha[b[i]] < removed:
            out += "0 "

        else:
            out += str(ha[b[i]] - removed + 1) + " "
            removed = ha[b[i]] + 1
    # print(out[:-1])
    pass
if __name__ == "__main__":
    main(10)