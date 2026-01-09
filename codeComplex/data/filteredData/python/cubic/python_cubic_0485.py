import math

def main(n):
    # Interpret n as grid size, with m = n and kk = 2*n (even, proportional to size)
    m = n
    kk = 2 * n

    # Deterministic generation of right and down cost matrices
    # right: n x m
    right = [[(i + j + 1) % 7 + 1 for j in range(m)] for i in range(n)]
    # down: (n-1) x m
    if n > 1:
        down = [[(i * 3 + j * 2 + 5) % 11 + 1 for j in range(m)] for i in range(n - 1)]

    else:
        down = []

    dp = [[math.inf for _ in range(m)] for _ in range(n)]
    dpCopy = [[math.inf for _ in range(m)] for _ in range(n)]

    for step in range(1, (kk // 2) + 1):
        for j in range(n):
            for k in range(m):
                if step == 1:
                    if j == 0:
                        if k == 0:
                            val = math.inf
                            if n > 1:
                                val = min(val, down[j][k])
                            if m > 1:
                                val = min(val, right[j][k])
                            dp[j][k] = min(dp[j][k], val)
                        elif k == m - 1:
                            val = math.inf
                            if m > 1:
                                val = min(val, right[j][k - 1])
                            if n > 1:
                                val = min(val, down[j][k])
                            dp[j][k] = min(dp[j][k], val)

                        else:
                            val = math.inf
                            val = min(val, right[j][k - 1])
                            val = min(val, right[j][k])
                            if n > 1:
                                val = min(val, down[j][k])
                            dp[j][k] = min(dp[j][k], val)
                    elif j == n - 1:
                        if k == 0:
                            val = math.inf
                            if n > 1:
                                val = min(val, down[j - 1][k])
                            if m > 1:
                                val = min(val, right[j][k])
                            dp[j][k] = min(dp[j][k], val)
                        elif k == m - 1:
                            val = math.inf
                            if m > 1:
                                val = min(val, right[j][k - 1])
                            if n > 1:
                                val = min(val, down[j - 1][k])
                            dp[j][k] = min(dp[j][k], val)

                        else:
                            val = math.inf
                            val = min(val, right[j][k - 1])
                            val = min(val, right[j][k])
                            if n > 1:
                                val = min(val, down[j - 1][k])
                            dp[j][k] = min(dp[j][k], val)
                    elif k == 0:
                        val = math.inf
                        if m > 1:
                            val = min(val, right[j][k])
                        if j > 0:
                            val = min(val, down[j - 1][k])
                        if j < n - 1:
                            val = min(val, down[j][k])
                        dp[j][k] = min(dp[j][k], val)
                    elif k == m - 1:
                        val = math.inf
                        if m > 1:
                            val = min(val, right[j][k - 1])
                        if j > 0:
                            val = min(val, down[j - 1][k])
                        if j < n - 1:
                            val = min(val, down[j][k])
                        dp[j][k] = min(dp[j][k], val)

                    else:
                        val = math.inf
                        val = min(val, right[j][k - 1])
                        val = min(val, right[j][k])
                        if j > 0:
                            val = min(val, down[j - 1][k])
                        if j < n - 1:
                            val = min(val, down[j][k])
                        dp[j][k] = min(dp[j][k], val)
                    continue

                if j == 0:
                    if k == 0:
                        candidates = []
                        if k + 1 < m:
                            candidates.append(dpCopy[j][k + 1] + right[j][k])
                        if j + 1 < n:
                            candidates.append(dpCopy[j + 1][k] + down[j][k])
                        if candidates:
                            dp[j][k] = min(candidates)
                    elif k == m - 1:
                        candidates = []
                        if k - 1 >= 0:
                            candidates.append(dpCopy[j][k - 1] + right[j][k - 1])
                        if j + 1 < n:
                            candidates.append(dpCopy[j + 1][k] + down[j][k])
                        if candidates:
                            dp[j][k] = min(candidates)

                    else:
                        candidates = []
                        if k - 1 >= 0:
                            candidates.append(dpCopy[j][k - 1] + right[j][k - 1])
                        if k + 1 < m:
                            candidates.append(dpCopy[j][k + 1] + right[j][k])
                        if j + 1 < n:
                            candidates.append(dpCopy[j + 1][k] + down[j][k])
                        if candidates:
                            dp[j][k] = min(candidates)
                elif j == n - 1:
                    if k == 0:
                        candidates = []
                        if j - 1 >= 0:
                            candidates.append(dpCopy[j - 1][k] + down[j - 1][k])
                        if k + 1 < m:
                            candidates.append(dpCopy[j][k + 1] + right[j][k])
                        if candidates:
                            dp[j][k] = min(candidates)
                    elif k == m - 1:
                        candidates = []
                        if j - 1 >= 0:
                            candidates.append(dpCopy[j - 1][k] + down[j - 1][k])
                        if k - 1 >= 0:
                            candidates.append(dpCopy[j][k - 1] + right[j][k - 1])
                        if candidates:
                            dp[j][k] = min(candidates)

                    else:
                        candidates = []
                        if j - 1 >= 0:
                            candidates.append(dpCopy[j - 1][k] + down[j - 1][k])
                        if k - 1 >= 0:
                            candidates.append(dpCopy[j][k - 1] + right[j][k - 1])
                        if k + 1 < m:
                            candidates.append(dpCopy[j][k + 1] + right[j][k])
                        if candidates:
                            dp[j][k] = min(candidates)
                elif k == 0:
                    candidates = []
                    if j - 1 >= 0:
                        candidates.append(dpCopy[j - 1][k] + down[j - 1][k])
                    if j + 1 < n:
                        candidates.append(dpCopy[j + 1][k] + down[j][k])
                    if k + 1 < m:
                        candidates.append(dpCopy[j][k + 1] + right[j][k])
                    if candidates:
                        dp[j][k] = min(candidates)
                elif k == m - 1:
                    candidates = []
                    if j - 1 >= 0:
                        candidates.append(dpCopy[j - 1][k] + down[j - 1][k])
                    if j + 1 < n:
                        candidates.append(dpCopy[j + 1][k] + down[j][k])
                    if k - 1 >= 0:
                        candidates.append(dpCopy[j][k - 1] + right[j][k - 1])
                    if candidates:
                        dp[j][k] = min(candidates)

                else:
                    candidates = []
                    if j - 1 >= 0:
                        candidates.append(dpCopy[j - 1][k] + down[j - 1][k])
                    if j + 1 < n:
                        candidates.append(dpCopy[j + 1][k] + down[j][k])
                    if k - 1 >= 0:
                        candidates.append(dpCopy[j][k - 1] + right[j][k - 1])
                    if k + 1 < m:
                        candidates.append(dpCopy[j][k + 1] + right[j][k])
                    if candidates:
                        dp[j][k] = min(candidates)

        for ii in range(n):
            for jj in range(m):
                dpCopy[ii][jj] = dp[ii][jj]

    if kk % 2 == 1:
        for i in range(n):
            # print(' '.join(['-1'] * m))
            pass
        return

    for i in range(n):
        row = []
        for j in range(m):
            if dp[i][j] == math.inf:
                row.append('-1')

            else:
                row.append(str(2 * dp[i][j]))
        # print(' '.join(row))
        pass
if __name__ == "__main__":
    main(5)