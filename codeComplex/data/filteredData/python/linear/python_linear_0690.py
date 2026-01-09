def main(n):
    # 根据规模 n 生成测试数据：构造一个在可行区间内的 s
    # 可行区间：2*n - 1 <= s <= n*(n+1)//2
    s_min = 2 * n - 1
    s_max = n * (n + 1) // 2
    if s_min > s_max:
        # 理论上不会发生，n>=1 时总有 s_min <= s_max
        # print("No")
        pass
        return

    # 这里选取中间值作为测试 s
    s = (s_min + s_max) // 2

    # 原逻辑开始
    if not 2 * n - 1 <= s <= n * (n + 1) // 2:
        # print('No')
        pass
        return
    # print('Yes')
    pass

    def ok(d):
        dep, cur, total_sum, m = 2, 1, 1, 0
        while cur + m < n:
            m += cur
            cur = min(n - m, cur * d)
            total_sum += cur * dep
            dep += 1
        return total_sum <= s

    l, r = 1, n
    while l < r:
        mid = (l + r) // 2
        if ok(mid):
            r = mid

        else:
            l = mid + 1

    # 下面会修改 n 的值，因此先保存原始 n 用于生成结构
    N = n

    a = [l - 1] * (N + 1)
    me = [i for i in range(N + 1)]
    total_sum = N * (N + 1) // 2
    low = 2
    n = N  # 接下来要在循环中减少 n

    while n > low and total_sum > s:
        dest = min(total_sum - s, n - low)
        total_sum -= dest
        me[n] -= dest
        a[me[n] + 1] += l
        a[me[n]] -= 1
        if not a[low]:
            low += 1
        n -= 1

    me = sorted(me[1:])
    l_ptr, dg = 0, 0
    for i in me[1:]:
        while me[l_ptr] < i - 1 or dg == r:
            dg = 0
            l_ptr += 1
        # print(l_ptr + 1, end=' ')
        pass
        dg += 1
    # print()
    pass


# 示例运行
if __name__ == "__main__":
    # 可以自由修改 n 的值进行测试
    main(10)