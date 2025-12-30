import random

def main(n):
    # 这里将 m 也设为 n，可以按需修改为其他规则
    m = n
    # 设置步数 k，可根据需要调整，这里用一个与 n 成比例的偶数
    k = 2 * n if n > 0 else 0
    if k == 0:
        return

    # 生成测试数据：权值为 1~9 的随机整数
    # ej: n 行，每行 m-1 个数（若 m>1），若 m==1 则为空列表
    ej = []
    for _ in range(n):
        if m > 1:
            ej.append([random.randint(1, 9) for _ in range(m - 1)])
        else:
            ej.append([])

    # ei: n-1 行，每行 m 个数（若 n>1），若 n==1 则为空列表
    ei = []
    for _ in range(n - 1):
        ei.append([random.randint(1, 9) for _ in range(m)])

    if k % 2:
        for _ in range(n):
            print(*[-1] * m)
        return

    inf = -1
    dp = [[inf] * (n * m) for _ in range(k // 2 + 1)]
    for t in range(n * m):
        dp[0][t] = 0

    for c in range(k // 2):
        for i in range(n):
            for j in range(m):
                t = i * m + j

                # 向下
                tt = (i + 1) * m + j
                if i + 1 < n:
                    cost = dp[c][t] + ei[i][j]
                    if dp[c + 1][tt] == -1 or dp[c + 1][tt] > cost:
                        dp[c + 1][tt] = cost

                # 向右
                tt = i * m + j + 1
                if j + 1 < m:
                    cost = dp[c][t] + ej[i][j]
                    if dp[c + 1][tt] == -1 or dp[c + 1][tt] > cost:
                        dp[c + 1][tt] = cost

                # 向上
                tt = (i - 1) * m + j
                if i - 1 >= 0:
                    cost = dp[c][t] + ei[i - 1][j]
                    if dp[c + 1][tt] == -1 or dp[c + 1][tt] > cost:
                        dp[c + 1][tt] = cost

                # 向左
                tt = i * m + j - 1
                if j - 1 >= 0:
                    cost = dp[c][t] + ej[i][j - 1]
                    if dp[c + 1][tt] == -1 or dp[c + 1][tt] > cost:
                        dp[c + 1][tt] = cost

    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            res[i][j] = dp[-1][i * m + j] * 2
        print(*res[i])


if __name__ == "__main__":
    # 示例：调用 main(4)，可自行修改 n
    main(4)