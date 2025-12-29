import random

def main(n):
    # 生成测试数据：
    # n 表示初始 a 的长度（去掉插入的 0 之前）
    # 生成严格递增且在区间 [1, M-1] 内的序列 a
    # 并生成一个略大于最大 a 的 M
    if n <= 0:
        return 0

    # 生成有序不重复随机序列
    # 为避免边界问题，设定最大值上限
    max_val = max(2 * n, n + 10)
    # 确保能生成 n 个不同位置
    positions = sorted(random.sample(range(1, max_val), n))
    a = positions[:]  # a[0..n-1]

    M = max_val + 5  # 保证 M > 所有 a[i]

    # 原始逻辑
    # 原代码对 n 做了 n += 1，并在开头插入 0
    # 这里保持一致：n_work 为插入 0 后的长度
    a_work = [0] + a
    n_work = n + 1

    lit = [0] * (n_work + 1)
    for i in range(1, n_work):
        if i % 2 == 0:
            lit[i] = lit[i - 1]
        else:
            lit[i] = lit[i - 1] + a_work[i] - a_work[i - 1]
    if n_work % 2 == 0:
        lit[n_work] = lit[n_work - 1]
    else:
        lit[n_work] = lit[n_work - 1] + M - a_work[n_work - 1]

    ans = lit[n_work]
    for i in range(n_work):
        pre_lit = lit[i]
        post_lit = M - a_work[i] - (lit[n_work] - lit[i])

        if i > 0 and a_work[i - 1] + 1 < a_work[i]:
            if i % 2 == 0:
                ans = max(ans, pre_lit + 1 + post_lit)
            else:
                ans = max(ans, pre_lit - 1 + post_lit)

        if (i + 1 < n_work and a_work[i] + 1 < a_work[i + 1]) or (i + 1 == n_work and a_work[n_work - 1] + 1 < M):
            if i % 2 == 0:
                ans = max(ans, pre_lit + post_lit + 1)
            else:
                ans = max(ans, pre_lit + post_lit - 1)

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)