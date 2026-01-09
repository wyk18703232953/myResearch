def main(n):
    # Interpret n as both dimensions of the grid: m = n, cols = n
    # Also set k proportional to n to scale the computation.
    m = n
    cols = n
    k = 2 * n  # even, and grows with n for scalability

    horizon = []
    for i in range(m):
        horizon.append([(i + j) % 7 + 1 for j in range(cols)])

    vertical = []
    for i in range(m - 1):
        vertical.append([(i * 3 + j * 5) % 9 + 1 for j in range(cols)])

    if k % 2 == 1:
        ans = [-1] * cols
        for _ in range(m):
            # print(" ".join(map(str, ans)))
            pass
        return

    direc = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    ans = [[0 for _ in range(cols)] for _ in range(m)]

    from copy import deepcopy

    for _ in range(k // 2):
        tempans = deepcopy(ans)
        for i in range(m):
            for j in range(cols):
                best = 2147483647
                for d in range(4):
                    neighi = i + direc[d][0]
                    neighj = j + direc[d][1]
                    if neighi < 0 or neighi >= m or neighj < 0 or neighj >= cols:
                        continue
                    base = tempans[neighi][neighj]
                    if d == 0:
                        base += 2 * horizon[neighi][neighj]
                    if d == 1:
                        base += 2 * horizon[neighi][neighj - 1]
                    if d == 2:
                        base += 2 * vertical[neighi - 1][neighj]
                    if d == 3:
                        base += 2 * vertical[neighi][neighj]
                    if base < best:
                        best = base
                ans[i][j] = best

    for row in ans:
        # print(" ".join(map(str, row)))
        pass
if __name__ == "__main__":
    main(5)