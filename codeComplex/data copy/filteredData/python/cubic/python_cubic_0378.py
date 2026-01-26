def main(n):
    # Deterministically set mod as a function of n
    mod = 10**9 + 7

    le = 500

    def pow_mod(x, y):  # x**y mod mod
        ans = 1
        x %= mod
        while y > 0:
            if y % 2 == 1:
                ans = (ans * x) % mod
            x = (x * x) % mod
            y //= 2
        return ans

    def inv(x):  # modular inverse assuming mod is prime
        return pow_mod(x, mod - 2)

    M = [1]  # i! mod mod
    mul = 1
    for i in range(1, le):
        mul = (mul * i) % mod
        M.append(mul)

    L0 = n // 2 + 3
    L1 = n + 1

    D = [[0 for _ in range(L1)] for _ in range(L0)]
    ND = [[0 for _ in range(L1)] for _ in range(L0)]

    INVS = [0] + [inv(i) for i in range(1, n + 1)]

    D[1][1] = 1
    for z in range(2, n + 1):  # total number of "computers"
        l0 = z // 2 + 3
        l1 = z + 1

        for i in range(l0):
            for j in range(l1):
                ND[i][j] = 0

        for i in range(l0):
            if i >= 1:
                ND[i][1] += D[i - 1][0] * (z - (i - 1))
                ND[i][1] %= mod

        for i in range(l0):
            for j in range(1, n + 1):
                ND[i][0] += D[i][j]
                ND[i][0] %= mod

        for i in range(l0):
            for j in range(l1):
                if j >= 2:
                    p = D[i][j - 1]
                    p *= (z - (i - 1))
                    p %= mod
                    p *= INVS[j] * 2
                    p %= mod
                    ND[i][j] += p
                    ND[i][j] %= mod

        for i in range(l0):
            for j in range(l1):
                D[i][j] = ND[i][j]

    ans = 0
    for i in range(L0):
        for j in range(1, L1):
            ans += D[i][j]
            ans %= mod

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(500)