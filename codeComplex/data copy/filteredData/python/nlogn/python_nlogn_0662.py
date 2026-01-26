def main(n):
    mod = 998244353

    # Generate deterministic P of length n with values in 1..n and some -1
    P = []
    for i in range(n):
        if i % 3 == 0:
            P.append(-1)

        else:
            # deterministic permutation-like pattern
            P.append((i * 2 + 1) % n + 1 if n > 0 else 1)

    INV = [None] * (n + 1)
    for i in range(1, n + 1):
        INV[i] = pow(i, mod - 2, mod)

    BLA = P.count(-1)

    if BLA == 0 or BLA == 1:
        ANS = 0

    else:
        LEFT = BLA * (BLA - 1) // 2 * INV[BLA] % mod
        AVEP = BLA * (BLA - 1) // 2 * pow(BLA - 1, mod - 2, mod)
        ANS = LEFT * AVEP % mod

    y = 1
    for i in range(BLA):
        y = y * (BLA - i) % mod

    KOSUU = pow(y, mod - 2, mod)

    BLALIST = [1] * (n + 1)
    NONBLA = []
    BLANUM = [0] * n
    for i in range(n):
        if P[i] != -1:
            BLALIST[P[i]] = 0
            BLANUM[i] = BLANUM[i - 1] if i > 0 else 0
            NONBLA.append(P[i])

        else:
            BLANUM[i] = (BLANUM[i - 1] if i > 0 else 0) + 1

    BLALIST[0] = 0
    for i in range(1, n + 1):
        BLALIST[i] = BLALIST[i - 1] + BLALIST[i]

    if BLA != 0:
        for i in range(n):
            if P[i] != -1:
                ANS = (
                    ANS
                    + (
                        BLANUM[i] * (BLA - BLALIST[P[i]])
                        + (BLA - BLANUM[i]) * BLALIST[P[i]]
                    )
                    * INV[BLA]
                ) % mod

    A = NONBLA

    if A == []:
        # print(ANS)
        pass
        return

    nA = len(A)
    MAXA = max(A)
    MINA = min(A)

    BIT = [0] * (MAXA - MINA + 2)

    for i in range(nA):
        bitobje = A[i] - MINA + 1

        x = bitobje
        while x != 0:
            ANS = (ANS - BIT[x]) % mod
            x -= (x & -x)

        x2 = MAXA - MINA + 1
        while x2 != 0:
            ANS = (ANS + BIT[x2]) % mod
            x2 -= (x2 & -x2)

        y = bitobje
        while y <= MAXA - MINA + 1:
            BIT[y] += 1
            y += (y & -y)

    # print(ANS)
    pass
if __name__ == "__main__":
    main(10)