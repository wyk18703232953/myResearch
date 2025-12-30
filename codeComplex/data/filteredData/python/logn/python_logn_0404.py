def solve_one_case(n, k):
    if n == 2 and k == 3:
        return "NO"
    if n <= 100:
        curr = 0
        for j in range(n):
            curr += pow(4, j)
        if curr < k:
            return "NO"
    curr = 0
    ans = 0
    while curr < k and ans < n:
        ans += 1
        curr += pow(2, ans) - 1
    if curr > k:
        ans -= 1
    return f"YES {n - ans}"


def main(n):
    """
    n: 规模参数，用于生成 t 个测试用例。
    这里约定：
      - 生成 t = n 个测试用例
      - 对于第 i 个用例：
          n_i = i + 1
          k_i = 2 * (i + 1) + 1
    """
    t = n
    results = []
    for i in range(t):
        ni = i + 1
        ki = 2 * (i + 1) + 1
        results.append(solve_one_case(ni, ki))
    print("\n".join(results))


if __name__ == "__main__":
    # 示例：以 n = 5 为规模运行
    main(5)