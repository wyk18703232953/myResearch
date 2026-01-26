def main(n):
    # Deterministically map n to (l, r)
    # Ensure l < r and both non-negative
    if n < 2:
        l, r = 0, 1

    else:
        l = n // 2
        r = l + (n % 5) + 1
    if l == r:
        # print(0)
        pass
        return
    binr, binl = list(bin(r)[2:]), list(bin(l)[2:])
    binl = ['0'] * (len(binr) - len(binl)) + binl
    for i in range(len(binl)):
        if binl[i] != binr[i]:
            binl = '1' * (len(binl[i:]))
            break
    # print(int(binl, 2))
    pass
if __name__ == "__main__":
    main(10)