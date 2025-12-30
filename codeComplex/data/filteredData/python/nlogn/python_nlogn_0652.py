def solve_one(n, k):
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
    n: 问题规模，同时也作为测试用例数量 t。
    自动生成 n 组 (n_i, k_i) 测试数据，并打印对应结果。
    """
    t = n

    # 根据规模 n 生成 t 组测试数据
    # 第 i 组数据采用：
    #   n_i = i + 1
    #   k_i = i
    # 可根据需要调整生成策略
    for i in range(t):
        ni = i + 1           # n_i 从 1,2,...,n
        ki = i               # 对应的 k_i 从 0,1,...,n-1
        res = solve_one(ni, ki)
        print(res)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行本地测试
    main(10)