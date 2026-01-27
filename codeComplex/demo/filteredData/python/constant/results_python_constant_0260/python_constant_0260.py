def main(n):
    # 解释规模含义：
    # n 表示原问题里的 n（区间上限），也是生成测试数据的规模参数
    # 构造一个确定性的单组测试数据 (n, pos, l, r)
    # 约束：1 <= l <= r <= n, 1 <= pos <= n
    if n < 1:
        return

    # 确定性构造 pos, l, r
    pos = n // 2 + 1          # 保证 1 <= pos <= n
    l = n // 3 + 1            # 保证 1 <= l <= n
    r = n - n // 4            # 保证 1 <= r <= n

    if l > r:
        l, r = r, l

    # 核心逻辑保持不变（单组数据）
    if l == 1 and r == n:
        ans = 0

    else:
        if l != 1 and r != n:
            ans = min(abs(l - pos), abs(r - pos)) + 2 + abs(r - l)

        else:
            if l == 1:
                ans = abs(pos - r) + 1

            else:
                ans = abs(pos - l) + 1

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：使用一个规模 n 调用
    main(10)