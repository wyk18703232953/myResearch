def main(n):
    global l, r, inv, fact
    p = 10**9 + 7
    max_n = 300001
    inv = [0] * max_n
    fact = [0] * max_n

    def ncr_util():
        inv[0] = inv[1] = 1
        fact[0] = fact[1] = 1
        for i in range(2, max_n):
            inv[i] = (inv[i % p] * (p - p // i)) % p
        for i in range(1, max_n):
            inv[i] = (inv[i - 1] * inv[i]) % p
            fact[i] = (fact[i - 1] * i) % p

    ncr_util()

    # Deterministic generation of l, r from n
    # Ensure l <= r and values are in a reasonable range
    l = n
    r = 2 * n + (n // 2)

    def solve():
        ans, a, b = 0, 0, 0
        mul = 2**60
        for i in range(60, -1, -1):
            ch1, ch2 = 0, 0
            if a + mul <= l:
                a += mul
                ch1 = 1
            if b + mul <= l:
                b += mul
                ch2 = 1
            if ch1 ^ ch2 == 1:
                ans += mul
            elif ch1 == 0 and ch2 == 0:
                if a + mul <= r:
                    a += mul
                    ans += mul
                elif b + mul <= r:
                    b += mul
                    ans += mul
            mul //= 2
        return ans

    return solve()


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    result = main(10**5)
    # print(result)
    pass