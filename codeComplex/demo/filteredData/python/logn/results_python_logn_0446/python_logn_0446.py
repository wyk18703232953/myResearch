def sol(n, k):
    p = 1
    q = 1
    acc = 0
    while n > 0 and k >= p:
        k -= p
        n -= 1
        if n >= 40:
            return n
        acc += q * (4 ** n - 1) // 3
        if k <= acc:
            return n
        p = 2 * p + 1
        q = 2 * q + 3
    return -1

def main(n):
    # 解释：将 n 视为测试用例数量 T
    # 为每个测试用例生成 (ni, ki)，保持确定性
    # 例如：
    #   ni = 1 + (i % 50)   控制在较小范围，避免 4**n 过大
    #   ki = i * i + 1
    results = []
    for i in range(1, n + 1):
        ni = 1 + (i % 50)
        ki = i * i + 1
        ans = sol(ni, ki)
        if ans == -1:
            results.append("NO")

        else:
            results.append("YES " + str(ans))
    # 统一一次性输出，方便计时
    # print("\n".join(results))
    pass
if __name__ == "__main__":
    main(10)