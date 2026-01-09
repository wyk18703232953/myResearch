def main(n):
    # Interpret n as the bit-length of r
    # Generate deterministic l, r based on n
    if n <= 0:
        # print(0)
        pass
        return
    r = (1 << n) - 1
    l = r // 3

    length = len(bin(r)[2:])
    ans = 0
    for x in range(0, length + 1):
        if (r >> x) & 1 == 1 and (l >> x) & 1 == 0:
            ans = max(ans, (1 << x) ^ ((1 << x) - 1))
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)