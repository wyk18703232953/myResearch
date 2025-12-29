import math
import random

# 第一段逻辑：间隔空闲时间计数
def logic1(n, L, a, segments):
    ed = 0
    ct = 0
    for j in range(n):
        t, l = segments[j]
        ct += (t - ed) // a
        ed = t + l
    t = L
    ct += (t - ed) // a
    return ct

# 第二段逻辑：3x3 模式匹配
def logic2(n, m, grid):
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    dp2 = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        s = grid[i]
        for j in range(m):
            if s[j] == '.':
                dp[i][j] = -1
            else:
                dp[i][j] = s[j]

    for i in range(0, n - 2):
        for j in range(0, m - 2):
            p = 0
            c = 0
            for k in range(i, i + 3):
                for h in range(j, j + 3):
                    p += 1
                    if p != 5:
                        if dp[k][h] == '#':
                            c += 1

            if c == 8:
                p = 0
                for k in range(i, i + 3):
                    for h in range(j, j + 3):
                        p += 1
                        if p != 5:
                            dp2[k][h] = '#'

    return "YES" if dp == dp2 else "NO"


# 第三段逻辑：原主程序逻辑
def logic3(n):
    if n == 3:
        return "1 1 3"
    res = []
    t = 1
    while t <= n:
        ct = math.ceil((n // t) / 2)
        for _ in range(ct):
            res.append(str(t))
        if ct == 2 and (n // t) % 2 != 0:
            t = t * 3
        else:
            t = t * 2
    return " ".join(res) + " "


def main(n: int):
    random.seed(0)

    # 1. 为逻辑1生成测试数据
    # n1 为段数，L1 为总长度，a 为每段长度单位
    n1 = max(1, n)
    L1 = n1 * 10
    a = max(1, n // 3)  # 避免为 0
    segments = []
    current_time = 0
    for _ in range(n1):
        start = current_time + random.randint(0, 2)  # 稍微有空隙
        length = random.randint(1, 3)
        segments.append((start, length))
        current_time = start + length
    ans1 = logic1(n1, L1, a, segments)

    # 2. 为逻辑2生成测试数据
    # 令网格规模与 n 相关但不要太大
    m2 = max(3, min(10, n))
    n2 = max(3, min(10, n))
    grid = []
    for _ in range(n2):
        row = []
        for _ in range(m2):
            row.append('#' if random.random() < 0.4 else '.')
        grid.append("".join(row))
    ans2 = logic2(n2, m2, grid)

    # 3. 逻辑3 的输出
    ans3 = logic3(n)

    # 输出所有结果（可以根据需要调整格式）
    print("Logic1 result:", ans1)
    print("Logic2 result:", ans2)
    print("Logic3 result:", ans3)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)