import sys

def main(n):
    # n controls the number of rows; keep m proportional for scalability
    if n <= 0:
        return
    m = max(2, n * 2)

    # Deterministic matrix generation similar in flavor to the commented example
    # MAT[i][k] = (i+1)^2 * (k+1)
    MAT = [[(i + 1) * (i + 1) * (k + 1) for k in range(m)] for i in range(n)]

    if n == 1:
        ANS = 10 ** 10
        for i in range(1, m):
            diff = MAT[0][i] - MAT[0][i - 1]
            if diff < 0:
                diff = -diff
            if ANS > diff:
                ANS = diff
        print(ANS)
        return

    EDGE0 = [[10 ** 10] * n for _ in range(n)]
    EDGE1 = [[10 ** 10] * n for _ in range(n)]
    MAX = 0
    MIN = 0

    if m != 1:
        for i in range(n):
            row_i = MAT[i]
            for j in range(n):
                row_j = MAT[j]
                # min over same column
                min_same = 10 ** 10
                for k in range(m):
                    diff = row_i[k] - row_j[k]
                    if diff < 0:
                        diff = -diff
                    if diff < min_same:
                        min_same = diff
                EDGE1[i][j] = min_same
                EDGE1[j][i] = min_same
                if EDGE1[i][j] > MAX:
                    MAX = EDGE1[i][j]

                # min over shifted column
                min_shift = 10 ** 10
                for k in range(1, m):
                    diff = row_i[k] - row_j[k - 1]
                    if diff < 0:
                        diff = -diff
                    if diff < min_shift:
                        min_shift = diff
                EDGE0[i][j] = min_shift
    else:
        for i in range(n):
            row_i = MAT[i]
            for j in range(n):
                row_j = MAT[j]
                min_same = 10 ** 10
                for k in range(m):
                    diff = row_i[k] - row_j[k]
                    if diff < 0:
                        diff = -diff
                    if diff < min_same:
                        min_same = diff
                EDGE1[i][j] = min_same
                EDGE1[j][i] = min_same
                if EDGE1[i][j] > MAX:
                    MAX = EDGE1[i][j]

    sys.setrecursionlimit(1 << 25)

    def Hamilton(start, USED, rest, last, weight, MEMO, n, EDGE0, EDGE1):
        idx = last * (1 << n) + USED
        if MEMO[idx] != 2:
            return MEMO[idx]
        if rest == 1:
            final = -1
            for i in range(n):
                if (USED & (1 << i)) == 0:
                    final = i
                    break

            if EDGE0[start][final] >= weight and EDGE1[last][final] >= weight:
                MEMO[idx] = 1
                return 1
            else:
                MEMO[idx] = 0
                return 0

        for j in range(n):
            if (USED & (1 << j)) == 0 and EDGE1[last][j] >= weight:
                NEXT = USED | (1 << j)
                if Hamilton(start, NEXT, rest - 1, j, weight, MEMO, n, EDGE0, EDGE1) == 1:
                    MEMO[idx] = 1
                    return 1

        MEMO[idx] = 0
        return 0

    while MAX != MIN:
        aveweight = (MAX + MIN + 1) // 2

        found = False
        size_memo = n * (1 << (n + 1))
        for start in range(n):
            MEMO = [2] * size_memo
            START = 1 << start
            if Hamilton(start, START, n - 1, start, aveweight, MEMO, n, EDGE0, EDGE1) == 1:
                MIN = aveweight
                found = True
                break
        if not found:
            MAX = aveweight - 1

    print(MAX)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)