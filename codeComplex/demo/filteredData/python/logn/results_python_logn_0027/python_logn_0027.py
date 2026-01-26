def main(n):
    # Interpret n as the number of bits; generate l, r with first n bits as 1
    if n <= 0:
        l = 0
        r = 0

    else:
        l = (1 << n) - 1
        # Ensure r >= l and differs at some higher bit position deterministically
        r = l

    if l == r:
        # print("0")
        pass

    else:
        i = 0
        j = 0
        ll = l
        rr = r
        while ll > 0 or rr > 0:
            i += 1
            if (ll & 1) ^ (rr & 1) == 1:
                j = i
            ll = ll >> 1
            rr = rr >> 1
        ans = 1
        for _ in range(0, j):
            ans = ans * 2
        ans -= 1
        # print(ans)
        pass
if __name__ == "__main__":
    main(10)