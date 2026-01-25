def main(n):
    # 为了得到确定性、可扩展的实验，我们需要从单一规模参数 n 构造原程序的两个输入：N 和 S。
    # 原程序第一个输入 n 表示树的节点数，这里用 N 表示，直接取 N = n。
    # S 必须满足区间 [2*N-1, N*(N+1)//2]，否则原程序直接输出 "No" 并退出。
    # 为了保证一定是 "Yes" 分支并触发完整算法逻辑，构造一个在范围中间偏上的 S。
    if n <= 0:
        return
    N = n
    min_s = 2 * N - 1
    max_s = N * (N + 1) // 2
    # 确定性地生成一个位于合法区间中的 S，这里取 max_s - floor(N/3)
    S = max_s - N // 3
    if S < min_s:
        S = min_s
    if not 2 * N - 1 <= S <= N * (N + 1) // 2:
        print('No')
        return
    print('Yes')

    def ok(d, N, S):
        dep, cur, total, m = 2, 1, 1, 0
        # 使用局部变量 nn 代替全局 n
        nn = N
        while cur + m < nn:
            m += cur
            cur = min(nn - m, cur * d)
            total += cur * dep
            dep += 1
        return total <= S

    # 二分查找最小 d
    l, r = 1, N
    while l < r:
        mid = (l + r) // 2
        if ok(mid, N, S):
            r = mid
        else:
            l = mid + 1

    # 下面的逻辑需要可变的 n 和 s，将其拷贝到局部变量
    n_work = N
    s_work = S

    a = [l - 1] * (n_work + 1)
    me = [i for i in range(n_work + 1)]
    total_sum = n_work * (n_work + 1) // 2
    low = 2
    while n_work > low and total_sum > s_work:
        dest = min(total_sum - s_work, n_work - low)
        total_sum -= dest
        me[n_work] -= dest
        a[me[n_work] + 1] += l
        a[me[n_work]] -= 1
        if not a[low]:
            low += 1
        n_work -= 1

    me_sorted = sorted(me[1:])
    l_idx = 0
    dg = 0
    for i in me_sorted[1:]:
        while me_sorted[l_idx] < i - 1 or dg == r:
            dg = 0
            l_idx += 1
        print(l_idx + 1, end=' ')
        dg += 1
    print()


if __name__ == "__main__":
    # 示例：使用规模 n = 10 运行一次
    main(10)