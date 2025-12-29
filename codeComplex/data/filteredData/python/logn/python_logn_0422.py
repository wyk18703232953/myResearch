def solve_case(n, k):
    if n >= 32:
        return "YES " + str(n - 1)
    else:
        ans = -1
        for i in range(1, n + 1):
            p = (4 ** i) - (2 ** (i + 1)) + 1
            p *= ((4 ** (n - i) - 1) // 3)
            g = ((4 ** i) - 1) // 3
            p += ((4 ** i) - 1) // 3
            g = ((4 ** i) - 1) // 3 - ((4 ** (i - 1) - 1) // 3)
            if g <= k and p >= k:
                ans = n - i
                break
        if ans != -1:
            return "YES " + str(ans)
        else:
            return "NO"


def main(n):
    """
    n: 规模参数，这里用作测试数据规模。
       生成 n 组测试数据 (n_i, k_i)，并输出对应结果。
    测试数据约定：
       第 i 组：n_i = i + 1, k_i = i
    """
    results = []
    for i in range(n):
        ni = i + 1
        ki = i
        results.append(solve_case(ni, ki))
    # 输出所有结果，每行一条
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例：调用 main(10) 生成 10 组测试并输出
    main(10)