import copy
from itertools import accumulate

def main(n):
    m = max(1, n // 3)
    k = max(1, n // 5)
    A = [(i * 2 + 3) % (k + 7) + 1 for i in range(n)]

    ANS = 0

    for i in range(m):
        B = copy.deepcopy(A)

        for j in range(i, n, m):
            B[j] -= k

        SUM = list(accumulate(B))
        SUMMIN = [float("inf")] * n + [0]

        if i == 0:
            SUMMIN[0] = 0

        for j in range(max(1, i), n):
            if j % m == i % m:
                SUMMIN[j] = min(SUMMIN[j - 1], SUM[j - 1])

            else:
                SUMMIN[j] = SUMMIN[j - 1]

        for j in range(i, n):
            ANS = max(ANS, SUM[j] - SUMMIN[j])

    # print(ANS)
    pass
if __name__ == "__main__":
    main(10)