import bisect

# 预处理素数（范围可按需要放大，这里给到 10^6 级别就够多数测试用）
def get_primes(limit):
    primes = [2]
    for i in range(3, limit + 1, 2):
        flag = False
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                flag = True
                break
        if not flag:
            primes.append(i)
    return primes


def build_prime_factor_func(primes):
    def primefactor(num):
        index = 0
        output = []
        while index < len(primes) and num >= primes[index] ** 2:
            times = 0
            while num % primes[index] == 0:
                num //= primes[index]
                times += 1
            if times & 1:
                output.append(primes[index])
            index += 1
        if num > 1:
            output.append(num)
        return tuple(output)

    return primefactor


def solve_one_case(n, k, arr, primefactor):
    fact = {}
    left = [[0 for _ in range(k + 1)] for _ in range(n)]
    dp = [[300000 for _ in range(k + 1)] for _ in range(n)]
    stack = [0]

    # 预处理 left 数组
    for i in range(n):
        factor = primefactor(arr[i])
        if factor in fact:
            bisect.insort(stack, fact[factor] + 1)
        fact[factor] = i
        for j in range(k + 1):
            if j < len(stack):
                left[i][j] = stack[-j - 1]

    # DP
    for i in range(n):
        for j in range(k + 1):
            for t in range(j + 1):
                l = left[i][t]
                if l > 0:
                    dp[i][j] = min(dp[l - 1][j - t] + 1, dp[i][j])
                else:
                    dp[i][j] = min(dp[i][j], 1)

    return dp[-1][-1]


def main(n):
    """
    n: 问题规模（数组长度）。
    该函数内部自动构造测试数据并运行一次原逻辑，返回结果。
    测试数据策略：
      - k 取 _min(20, n)。
      - arr[i] 在 1..1e6 内随机/构造，这里简单构造成 i+1 和一些平方数，保证有重复因子结构。
    """
    # 生成素数表和分解函数
    primes = get_primes(10 ** 6)
    primefactor = build_prime_factor_func(primes)

    # 构造测试数据
    k = min(20, n)
    # 构造 arr：混合一些平方数和线性数，制造非平方因子冲突
    arr = []
    for i in range(n):
        val = (i + 1)
        if i % 5 == 0:
            val *= val  # 制造平方
        arr.append(val)

    # 调用一次原逻辑
    ans = solve_one_case(n, k, arr, primefactor)
    print(ans)


# 示例：直接运行 main(10) 做一次测试
if __name__ == "__main__":
    main(10)