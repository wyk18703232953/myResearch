def main(n):
    """
    n: 规模参数，用来生成测试数据。
       我们构造 s，使得 0 <= s <= n。这里简单设 s = n // 2。
    程序逻辑与原始代码等价：计算满足 x >= s + sum_digits(x) 的 x 在 [1, n] 内的个数。
    """

    # 根据规模 n 生成测试数据
    s = n // 2

    lo, hi = s, n
    ans = n + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        z = sum(map(int, str(mid)))
        if mid >= s + z:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    # 返回原程序的输出结果
    return n - ans + 1


if __name__ == "__main__":
    # 示例：用某个规模调用 main，并打印结果
    test_n = 10**6
    print(main(test_n))