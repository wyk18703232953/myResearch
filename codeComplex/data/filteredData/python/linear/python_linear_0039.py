def main(n):
    # 确定性数据生成
    # 令 k 与 n 相关，保证 1 <= k <= n 且不过大
    if n <= 0:
        # print(-1, -1)
        pass
        return
    k = max(1, n // 3)
    # 生成数组 a，元素值在 [1, n] 范围内，使用确定性规则
    # 将 a 构造为前 n 个按 (i % (n // 2 + 1)) + 1 映射的值，保证有重复
    mod_base = n // 2 + 1
    a = [(i % mod_base) + 1 for i in range(n)]

    i = 0
    d = 0
    x = -1
    y = -1
    s = [0] * (10**5 + 1)

    for j in range(len(a)):
        val = a[j]
        s[val] += 1
        i += 1
        if s[val] == 1:
            d += 1
        if i == 1:
            x = j + 1
        if d == k:
            y = j + 1
            break

    while k != 1 and x != -1 and s[a[x - 1]] - 1 != 0:
        s[a[x - 1]] -= 1
        x += 1

    if x == -1 or y == -1:
        x = -1
        y = -1

    # print(x, y)
    pass
if __name__ == "__main__":
    # 示例：可以根据需要修改 n 以做规模化实验
    main(10)