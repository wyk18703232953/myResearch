def main(n):
    # 输入规模含义：
    # n = 原程序中的 n（列表长度），k 固定取 n//2（且至少为 1）
    if n <= 0:
        return

    k = max(1, n // 2)

    # 构造与原程序等价的输入：
    # 构造 n 行，每行两个整数 (x, y)
    # 规则完全确定：x = n - i, y = i % 5
    a = [[n - i, i % 5] for i in range(n)]

    # 原程序逻辑
    a = sorted(a, key=lambda x: (-x[0], x[1]))
    p, t = -1, -1
    ans = 0
    if k <= n:
        p, t = a[k - 1]
    for x, y in a:
        if x == p and y == t:
            ans += 1
    print(ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以做时间复杂度实验
    main(10)