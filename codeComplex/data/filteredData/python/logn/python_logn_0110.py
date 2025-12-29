def main(n: int):
    """
    n 为规模参数，用来生成测试数据 (l, r)。
    这里约定：
    - 生成的区间为 [l, r]，满足 0 <= l <= r
    - r 的最大值规模约为 2^n - 1
    测试数据策略示例：
      若 n <= 1: 使用固定小例子
      若 n >  1: 令 r = 2^n - 1, l = 2^(n-1)
    """
    if n <= 0:
        l, r = 0, 0
    elif n == 1:
        # 简单边界例子
        l, r = 0, 1
    else:
        r = (1 << n) - 1
        l = 1 << (n - 1)

    # 原逻辑开始
    if l == r:
        ans = 0
    else:
        a = bin(l)[2:]
        b = bin(r)[2:]
        x = len(a)
        y = len(b)
        if x != y:
            ans = 0
            for i in range(y):
                ans += (2 ** i)
        else:
            for i in range(x):
                if a[i] != b[i]:
                    ind = i
                    break
            l2 = x - ind
            ans = 0
            for i in range(l2):
                ans += (2 ** i)

    print(ans)


if __name__ == "__main__":
    # 示例：可以修改这里的 n 来测试不同规模
    main(5)