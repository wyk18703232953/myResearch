def tonum(count):
    return (count - 1) // 3


def check(n, k, logdivl):
    divl = 2 ** logdivl

    min_k = 2 ** (logdivl + 1) - 2 - logdivl
    max_k = tonum(
        divl * divl
        + (divl * divl - (2 * divl - 1)) * ((2 ** (n - logdivl)) ** 2 - 1)
    )
    return min_k <= k <= max_k


def solve(n, k):
    if k == 1:
        return n - 1

    if n > 100:
        return n - 1

    if ((2 ** (n - 1)) ** 2 - 1) // 3 + 1 >= k:
        return n - 1

    for logdivl in range(1, n + 1):
        if check(n, k, logdivl):
            return n - logdivl

    return None


def main(n):
    """
    根据规模 n 生成测试数据并执行原逻辑。
    测试数据规则：对 k 从 1 到 n 依次测试。
    """
    results = []
    for k in range(1, n + 1):
        ans = solve(n, k)
        if ans is not None:
            results.append(("YES", k, ans))

        else:
            results.append(("NO", k, None))
    return results


if __name__ == "__main__":
    # 示例运行：以 n=10 生成测试数据并打印结果
    n = 10
    res = main(n)
    for status, k, ans in res:
        if status == "YES":
            # print(f"k={k}: YES {ans}")
            pass

        else:
            # print(f"k={k}: NO")
            pass