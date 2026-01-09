def main(n):
    # Deterministic data generation for time complexity experiments:
    # Interpret n as the maximum possible value for a and b.
    # Generate a and b as two deterministic integers based on n.
    if n < 2:
        a, b = 0, 0

    else:
        a = n // 3
        b = (2 * n) // 3 + (n % 2)

    # Core algorithm from original program
    a, b = min(a, b), max(a, b)

    bina = str(bin(a))[2:]
    binb = str(bin(b))[2:]

    lena = len(bina)
    lenb = len(binb)

    ans = 0
    if lena != lenb:
        ans = 2 ** lenb - 1

    else:
        a_str = '0' * (lena - lenb) + bina
        for i in range(lenb):
            if (bool(int(bina[i])) != bool(int(binb[i]))):
                ans = 2 ** (lenb - i) - 1
                break

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10_000)