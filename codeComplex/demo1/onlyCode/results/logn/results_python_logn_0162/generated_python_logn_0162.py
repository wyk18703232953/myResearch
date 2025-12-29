def main(n):
    # 生成测试数据：根据规模 n 构造 (n, k)
    # 原代码逻辑是对 n-1 和 k-1 做运算，因此这里选择一个与 n 同尺度的 k
    # 例如设 k = n（至少为 1）
    k = max(1, n)

    # 以下为原始逻辑（去掉 input，直接使用 n, k）
    n, k = n - 1, k - 1
    l = 0
    r = k
    g = k * (k + 1) // 2
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if (g - m * (m + 1) // 2) >= n:
            ans = k - m
            l = m + 1
        else:
            r = m - 1

    print(ans)


if __name__ == "__main__":
    # 示例调用：可修改为任意规模 n
    main(10)