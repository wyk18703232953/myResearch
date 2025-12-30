def main(n):
    # 这里的 n 作为“规模”参数，用来生成测试数据（k）
    # 原代码中 n,k 来自输入，这里我们固定一种生成方式：
    #   - 用传入的 n 作为原始的 n
    #   - 用 k = n 作为原始的 k（也可以根据需要改成其他函数关系）
    k = n

    # 对应原始程序开头：n,k = n-1, k-1
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


# 示例调用：
# main(10)