def solve_one_case(n, k):
    if n > 35:
        m = n - 1
        return "YES " + str(m)
    if k > (4 ** n - 1) // 3:
        return "NO"
    ans = None
    total = (4 ** n - 1) // 3
    for a in range(n):
        can = (2 ** (n - a + 1) - 1) * (4 ** a - 1) // 3
        min_val = 2 ** (n - a + 1) - 2 - n + a
        if total - can >= k >= min_val:
            ans = a
            break
    if ans is not None:
        return "YES " + str(ans)
    else:
        return "NO"


def main(n):
    """
    n 为规模参数，这里用 n 生成 n 组测试数据：
    第 i 组数据取:
        ni = i + 1
        ki = min(i + 1, (4**ni - 1)//3)  保证 k 不超过上界
    """
    t = n
    for i in range(t):
        ni = i + 1
        limit = (4 ** ni - 1) // 3
        ki = min(i + 1, limit)
        res = solve_one_case(ni, ki)
        print(res)


if __name__ == "__main__":
    # 示例：用 n=5 作为规模运行
    main(5)