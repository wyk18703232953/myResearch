def main(n):
    # 确定性生成 a, b，满足不同分支场景且随 n 可规模化
    # 设定四种模式循环出现：
    # 1: (a>1, b==1), 2: (a==1, b>1), 3: (a==1, b==1), 4: (a>1, b>1)
    mode = n % 4
    if mode == 1:
        a, b = max(2, n // 3 + 1), 1
    elif mode == 2:
        a, b = 1, max(2, n // 3 + 1)
    elif mode == 3:
        a, b = 1, 1

    else:
        a, b = max(2, n // 3 + 1), max(2, n // 4 + 1)

    # 原始逻辑
    if (n == 3 or n == 2) and (a == 1 and b == 1):
        # print("NO")
        pass
        return
    g = [[0 for _ in range(n)] for _ in range(n)]
    if a > 1 and b == 1:
        for i in range(n - a - 1, -1, -1):
            g[i][i + 1] = g[i + 1][i] = 1
    elif b > 1 and a == 1:
        a, b = b, a
        for i in range(n - a - 1, -1, -1):
            g[i][i + 1] = g[i + 1][i] = 1
        for i in range(n):
            for j in range(n):
                if g[i][j] == 0:
                    g[i][j] = 1
                elif g[i][j] == 1:
                    g[i][j] = 0
        for i in range(n):
            g[i][i] = 0
    elif a == 1 and b == 1:
        for i in range(n - 1):
            g[i][i + 1] = g[i + 1][i] = 1
    elif a > 1 and b > 1:
        # print("NO")
        pass
        return
    # print("YES")
    pass
    for i in range(n):
        for j in range(n):
            # print(g[i][j], end='')
            pass
        # print()
        pass
if __name__ == "__main__":
    # 示例规模调用，可按需修改
    main(10)