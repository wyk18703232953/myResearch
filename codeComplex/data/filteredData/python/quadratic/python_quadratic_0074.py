def nCr(n, r):
    from math import factorial
    f, m = factorial, 1
    for i in range(n, n - r, -1):
        m *= i
    return int(m // f(r))


def main(n):
    # 解释规模映射：
    # n >= 2
    #   - 数组 a 的长度 = n
    #   - 查询个数 q = n
    if n < 2:
        n = 2

    # 构造数组 a（长度为 n），元素为 1..n 的一个确定性排列：
    # 这里使用简单的“交错”构造，避免有序或完全逆序：
    a = [0] * n
    left, right = 1, n
    for i in range(n):
        if i % 2 == 0:
            a[i] = left
            left += 1
        else:
            a[i] = right
            right -= 1

    ans = []
    tem = 0
    mem = [0] * (n + 1)

    # 原始前半段逻辑，完全保持不变
    for i in range(n):
        for j in range(a[i] - 1, 0, -1):
            if not mem[j]:
                tem += 1
        mem[a[i]] = 1

    # 构造 q = n 个查询 (l, r)，1 <= l <= r <= n
    # 使用确定性模式遍历不同区间：
    queries = []
    q = n
    for i in range(q):
        l = (i % n) + 1
        # r 至少为 l，且不超过 n
        r_span = (i // 2) % n
        r = l + r_span
        if r > n:
            r = n
        if r < l:
            r = l
        queries.append((l, r))

    # 原始后半段逻辑
    for l, r in queries:
        tem += nCr(r - l + 1, 2)
        ans.append('odd' if tem % 2 else 'even')

    # 输出结果，供实验统计使用
    print('\n'.join(ans))


if __name__ == "__main__":
    # 示例：可根据需要修改 n 来做规模实验
    main(10)