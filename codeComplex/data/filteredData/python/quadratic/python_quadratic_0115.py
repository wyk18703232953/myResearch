def main(n):
    # n: number of distinct items
    # define m as a scalable function of n
    if n <= 0:
        print(0)
        return

    m = 3 * n  # total events, linear in n

    # deterministic generation of tL0 with values in [1, n]
    tL0 = [(i % n) + 1 for i in range(m)]

    tL = [0] * n
    score = 0

    for i in range(m):
        tL[tL0[i] - 1] += 1
        if 0 not in tL:
            score += 1
            for j in range(n):
                tL[j] = tL[j] - 1

    print(score)


if __name__ == "__main__":
    main(5)