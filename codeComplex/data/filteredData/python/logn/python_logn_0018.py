def main(n):
    # Interpret n as the maximum possible value for r.
    # Generate deterministic l and r with 0 <= l < r <= n
    # Ensure meaningful behavior for n < 2
    if n < 2:
        l, r = 0, 1

    else:
        l = n // 3
        r = n

    if l == r:
        # print(0)
        pass
        return

    binr, binl = bin(r)[2:], bin(l)[2:]
    binl = '0' * (len(binr) - len(binl)) + binl

    for i in range(len(binl)):
        if binl[i] != binr[i]:
            binl = '1' * len(binl[i:])
            break

    # print(int(binl, 2))
    pass
if __name__ == "__main__":
    main(10**6)