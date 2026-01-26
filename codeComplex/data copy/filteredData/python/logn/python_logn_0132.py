def main(n):
    # 为给定规模 n 自动生成测试数据 (n, k)
    # 这里选择一个简单策略：令 k = n//2 + 1，但保证至少为 2
    if n <= 1:
        k = 1

    else:
        k = max(2, n // 2 + 1)

    # 原始逻辑开始
    n_val = n
    k_val = k

    if n_val == 1:
        # print(0)
        pass
        return

    if n_val - 1 > (1 + k_val - 1) * (k_val - 1) // 2:
        # print(-1)
        pass
        return

    n_val -= 1
    k_val -= 1
    l, r = 0, k_val + 1

    while r - l > 1:
        m = (l + r) // 2
        if (m + k_val) * (k_val - m + 1) // 2 >= n_val:
            l = m

        else:
            r = m

    # print(k_val - l + 1)
    pass


# 示例：如需直接运行，可以调用 main(10) 等
if __name__ == "__main__":
    main(10)