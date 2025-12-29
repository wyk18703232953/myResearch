def solve(n, k):
    # 原逻辑：给定 n, k 计算答案
    l = 0
    r = n
    while r - l > 1:
        mid = (r + l) // 2
        a = n - mid
        if ((1 + a) * a) // 2 >= k + mid:
            l = mid
        else:
            r = mid
    return l


def main(n):
    """
    n: 规模参数，用于生成测试数据
    这里约定将 k 设置为 1..n 之中的某个值，
    示例中选择 k = n // 2（至少为 1）。
    """
    if n <= 0:
        return

    k = max(1, n // 2)  # 生成与规模相关的 k
    ans = solve(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例调用：可修改 n 以改变规模
    main(10)