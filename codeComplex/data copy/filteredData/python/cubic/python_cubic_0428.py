def aburrimin(x, y, n, m, costder, costaba, dp):
    dists = []
    vals = []
    if x != 0:  # izq
        dis = costder[y][x - 1]
        dists.append(dis)
        vals.append(dis + dp[y][x - 1])
    if y != 0:  # arri
        dis = costaba[y - 1][x]
        dists.append(dis)
        vals.append(dis + dp[y - 1][x])
    if y < n - 1:  # aba
        dis = costaba[y][x]
        dists.append(dis)
        vals.append(dis + dp[y + 1][x])
    if x < m - 1:  # der
        dis = costder[y][x]
        dists.append(dis)
        vals.append(dis + dp[y][x + 1])

    mindis = min(dists)
    return min(mindis + dp[y][x], min(vals))


def main(n):
    if n < 2:
        n = 2
    # Map n to grid size and k:
    # Use n as both rows and columns, and k proportional to n
    rows = n
    cols = n
    k = 2 * n  # ensure even, and scalable with n

    # Deterministic generation of costder and costaba
    # costder: rows x cols
    costder = [[(i * cols + j) % 7 + 1 for j in range(cols)] for i in range(rows)]
    # costaba: (rows-1) x cols
    costaba = [[((i + 1) * cols + j * 2) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]

    # The original logic assumes k is even; here k is constructed as even
    k //= 2

    for ren in range(len(costder)):
        for col in range(len(costder[ren])):
            costder[ren][col] *= 2
    for ren in range(len(costaba)):
        for col in range(len(costaba[ren])):
            costaba[ren][col] *= 2

    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    dptemp = [[0 for _ in range(cols)] for _ in range(rows)]

    for _ in range(k):
        for y in range(rows):
            for x in range(cols):
                dptemp[y][x] = aburrimin(x, y, rows, cols, costder, costaba, dp)
        dp, dptemp = dptemp, dp

    for ren in dp:
        for num in ren:
            # print(num, end=' ')
            pass
        # print()
        pass
if __name__ == "__main__":
    # Example scalable call; adjust n to change input size
    main(5)