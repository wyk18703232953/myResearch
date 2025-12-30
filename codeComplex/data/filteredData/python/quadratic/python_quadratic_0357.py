import random

def main(n: int):
    # 生成一个 n 行 m 列的随机 '*' / '.' 网格
    # 这里简单设 m = n，可以按需修改为其他关系
    m = n
    s = []
    for _ in range(n):
        # 随机生成一行：'*' 和 '.' 各 50% 概率
        row = ['*' if random.random() < 0.5 else '.' for _ in range(m)]
        s.append(row)

    # 以下基本保持原逻辑不变，只是去掉了 input 相关部分
    t = [[1000] * m for _ in range(n)]
    ok1 = [[0] * m for _ in range(n)]
    ok2 = [[0] * m for _ in range(n)]

    # 横向扫描，更新十字臂长度下界
    for i in range(n):
        si = s[i]
        c = 0
        for j in range(m):
            if si[j] == "*":
                c += 1
            else:
                c = 0
            t[i][j] = min(t[i][j], c)
        c = 0
        for j in range(m - 1, -1, -1):
            if si[j] == "*":
                c += 1
            else:
                c = 0
            t[i][j] = min(t[i][j], c)

    # 纵向扫描，更新十字臂长度下界
    for j in range(m):
        c = 0
        for i in range(n):
            if s[i][j] == "*":
                c += 1
            else:
                c = 0
            t[i][j] = min(t[i][j], c)
        c = 0
        for i in range(n - 1, -1, -1):
            if s[i][j] == "*":
                c += 1
            else:
                c = 0
            t[i][j] = min(t[i][j], c)

    ans = []
    for i in range(n):
        for j in range(m):
            tij = t[i][j] - 1
            if tij >= 1:
                ans.append((i + 1, j + 1, tij))
                ok1[max(0, i - tij)][j] += 1
                if i + tij + 1 < n:
                    ok1[i + tij + 1][j] -= 1
                ok2[i][max(0, j - tij)] += 1
                if j + tij + 1 < m:
                    ok2[i][j + tij + 1] -= 1

    for i in range(1, n):
        for j in range(1, m):
            ok1[i][j] += ok1[i - 1][j]
            ok2[i][j] += ok2[i][j - 1]

    for i in range(n):
        for j in range(m):
            if s[i][j] == "*":
                if not (ok1[i][j] or ok2[i][j]):
                    print(-1)
                    return

    k = len(ans)
    print(k)
    for ans0 in ans:
        print(*ans0)


if __name__ == "__main__":
    # 示例：调用 main(5) 生成规模为 5 的随机测试数据并运行
    main(5)