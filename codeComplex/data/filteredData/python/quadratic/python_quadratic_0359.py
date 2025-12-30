import sys
import random

def main(n):
    # 生成测试数据：n 行 n 列的随机 '.' / '*' 网格
    # 你也可以按需要改成确定性生成
    m = n
    chars = ['.', '*']
    s = [[random.choice(chars) for _ in range(m)] for _ in range(n)]

    u = [[-1 for _ in range(m)] for _ in range(n)]
    d = [[-1 for _ in range(m)] for _ in range(n)]
    l = [[-1 for _ in range(m)] for _ in range(n)]
    r = [[-1 for _ in range(m)] for _ in range(n)]

    # 向上连续 '*' 数量
    for i in range(m):
        acum = 0
        for j in range(n):
            if s[j][i] == ".":
                acum = 0
            else:
                acum += 1
            u[j][i] = acum

    # 向下连续 '*' 数量
    for i in range(m):
        acum = 0
        for j in range(n - 1, -1, -1):
            if s[j][i] == ".":
                acum = 0
            else:
                acum += 1
            d[j][i] = acum

    # 向左连续 '*' 数量
    for i in range(n):
        acum = 0
        for j in range(m):
            if s[i][j] == ".":
                acum = 0
            else:
                acum += 1
            l[i][j] = acum

    # 向右连续 '*' 数量
    for i in range(n):
        acum = 0
        for j in range(m - 1, -1, -1):
            if s[i][j] == ".":
                acum = 0
            else:
                acum += 1
            r[i][j] = acum

    ans = []
    t1 = [[0 for _ in range(m)] for _ in range(n)]
    t2 = [[0 for _ in range(m)] for _ in range(n)]

    # 计算所有可能的十字中心和臂长
    for i in range(n):
        for j in range(m):
            d1 = min(l[i][j], r[i][j], u[i][j], d[i][j]) - 1
            if d1 > 0:
                ans.append([i + 1, j + 1, d1])
                if 0 <= i + d1 < n:
                    t1[i + d1][j] += 1
                if 0 <= i - d1 < n:
                    t1[i - d1][j] -= 1
                if 0 <= j - d1 < m:
                    t2[i][j - d1] += 1
                if 0 <= j + d1 < m:
                    t2[i][j + d1] -= 1

    dp = [['.' for _ in range(m)] for _ in range(n)]

    # 按水平方向前缀和恢复覆盖情况
    for i in range(n):
        acum = 0
        for j in range(m):
            acum += t2[i][j]
            if acum != 0 or t2[i][j] != 0:
                dp[i][j] = '*'

    # 按竖直方向前缀和恢复覆盖情况
    for i in range(m):
        acum = 0
        for j in range(n):
            acum += t1[j][i]
            if acum != 0 or t1[j][i] != 0:
                dp[j][i] = '*'

    # 校验能否由若干十字构成原图
    if dp != s:
        print(-1)
        return

    print(len(ans))
    for item in ans:
        print(*item)


if __name__ == "__main__":
    # 举例：规模为 5
    main(5)