from copy import deepcopy
import random


def main(n):
    # 生成规模参数：
    # m: 行数，n: 列数，k: 步数（必须是偶数才有解）
    m = n
    k = 2 * (n // 2 + 1)  # 生成一个与 n 同数量级的偶数步数

    # 生成测试数据：边权均为 1~9 的正整数
    horizon = [[random.randint(1, 9) for _ in range(n - 1)] for _ in range(m)]
    vertical = [[random.randint(1, 9) for _ in range(n)] for _ in range(m - 1)]

    # 原逻辑：k 为奇数时无法回到原点，答案为 -1
    if k % 2 == 1:
        ans = [-1] * n
        for _ in range(m):
            print(" ".join(map(str, ans)))
        return

    direc = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    ans = [[0 for _ in range(n)] for _ in range(m)]

    for _ in range(k // 2):
        tempans = deepcopy(ans)
        for i in range(m):
            for j in range(n):
                ans[i][j] = 2147483647
                for d in range(4):
                    neighi = i + direc[d][0]
                    neighj = j + direc[d][1]
                    if neighi < 0 or neighi >= m or neighj < 0 or neighj >= n:
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
                    ans[i][j] = min(ans[i][j], base)

    for row in ans:
        print(" ".join(map(str, row)))


# 示例调用
if __name__ == "__main__":
    main(5)