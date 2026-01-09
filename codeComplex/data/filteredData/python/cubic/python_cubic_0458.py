import sys

def main(n):
    # Interpret n as grid size; keep k fixed to preserve algorithm shape
    if n <= 0:
        return
    rows = n
    cols = n
    k = 10  # even, so paths of length k are considered

    # Deterministic generation of l1 (horizontal edges) and l2 (vertical edges)
    # l1: rows x cols
    # l2: (rows-1) x cols
    l1 = [[(i * cols + j) % 9 + 1 for j in range(cols)] for i in range(rows)]
    if rows > 1:
        l2 = [[((i + 1) * cols + j) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]

    else:
        # When n == 1, there are no vertical edges; create empty structure
        l2 = []

    inf = 10 ** 18

    def check(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # dp[i][j][t]: minimum cost to take t steps starting from (i, j)
    # t ranges from 0..k//2; only 1..k//2 are used, but allocate full for clarity
    max_half = k // 2
    dp = [[[inf] * (max_half + 1) for _ in range(cols)] for _ in range(rows)]

    # Initialize dp for 1 step
    for i in range(rows):
        for j in range(cols):
            # move right
            if check(i, j + 1):
                if l1[i][j] < dp[i][j][1]:
                    dp[i][j][1] = l1[i][j]
            # move left
            if check(i, j - 1):
                if l1[i][j - 1] < dp[i][j][1]:
                    dp[i][j][1] = l1[i][j - 1]
            # move down
            if check(i + 1, j):
                if l2[i][j] < dp[i][j][1]:
                    dp[i][j][1] = l2[i][j]
            # move up
            if check(i - 1, j):
                if l2[i - 1][j] < dp[i][j][1]:
                    dp[i][j][1] = l2[i - 1][j]

    # DP transitions for more steps
    for steps in range(2, max_half + 1):
        for i in range(rows):
            for j in range(cols):
                best = dp[i][j][steps]
                # right
                if check(i, j + 1):
                    cost = l1[i][j] + dp[i][j + 1][steps - 1]
                    if cost < best:
                        best = cost
                # left
                if check(i, j - 1):
                    cost = l1[i][j - 1] + dp[i][j - 1][steps - 1]
                    if cost < best:
                        best = cost
                # down
                if check(i + 1, j):
                    cost = l2[i][j] + dp[i + 1][j][steps - 1]
                    if cost < best:
                        best = cost
                # up
                if check(i - 1, j):
                    cost = l2[i - 1][j] + dp[i - 1][j][steps - 1]
                    if cost < best:
                        best = cost
                dp[i][j][steps] = best

    ans = [[inf] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if k % 2 == 1:
                ans[i][j] = -1

            else:
                val = dp[i][j][max_half]
                if val >= inf:
                    ans[i][j] = -1

                else:
                    ans[i][j] = 2 * val

    out_lines = []
    for row in ans:
        out_lines.append(" ".join(str(x) for x in row))
    sys.stdout.write("\n".join(out_lines) + ("\n" if out_lines else ""))


if __name__ == "__main__":
    # Example deterministic call for timing/experiments
    main(5)