def main(n: int):
    # 这里根据 n 自动生成一组 (a, b) 测试数据
    # 规则只是示例，可按需要调整：
    # - 优先生成合法情况，保证能输出 "YES" 和矩阵
    # - 偶尔生成非法情况，测试 "NO" 分支
    if n < 2:
        # n 太小，强制构造一个明显非法的情况
        a, b = 2, 2
    elif n % 5 == 0:
        # 构造非法情况，用来触发 NO
        a, b = 2, 2
    elif n % 3 == 0:
        # 构造 a=1 的合法情况
        a, b = 1, max(1, n // 2)

    else:
        # 构造 b=1 的合法情况
        a, b = max(1, n // 2), 1

    # 原始逻辑开始
    if a > 1 and b > 1:
        # print("NO")
        pass
        return
    if 2 <= n <= 3 and a == b == 1:
        # print("NO")
        pass
        return
    # print("YES")
    pass

    if b == 1:
        adj = [[0] * n for _ in range(n)]
        conn = n
        for i in range(n - 1):
            if conn == a:
                break
            adj[i][i + 1] = adj[i + 1][i] = 1
            conn -= 1
            if conn == a:
                break
    elif a == 1:
        adj = [[1] * n for _ in range(n)]
        conn = n
        for i in range(n):
            adj[i][i] = 0
        for i in range(n - 1):
            if conn == b:
                break
            adj[i][i + 1] = adj[i + 1][i] = 0
            conn -= 1
            if conn == b:
                break

    else:
        # 理论上前面已排除 a>1 且 b>1 的情况，这里只是防御性代码
        return

    for row in adj:
        # print(*row, sep='')
        pass


# 示例：直接运行时给一个默认规模
if __name__ == "__main__":
    main(5)