import bisect
import random


# 预处理素数
prime = [2]
for i in range(3, 4 * 10**3, 2):
    if i % 2 == 0:
        continue
    flag = False
    for j in range(3, int(i**0.5) + 1, 2):
        if i % j == 0:
            flag = True
            break
    if not flag:
        prime.append(i)


def primefactor(num):
    index = 0
    output = []
    while index < len(prime) and num >= prime[index] ** 2:
        times = 0
        while num % prime[index] == 0:
            num //= prime[index]
            times += 1
        if times & 1:
            output.append(prime[index])
        index += 1
    if num > 1:
        output.append(num)
    return tuple(output)


def solve_single_case(n, k, arr):
    seg = 1
    fact = {}
    left = [[0 for _ in range(k + 1)] for _ in range(n)]
    dp = [[300000 for _ in range(k + 1)] for _ in range(n)]

    stack = [0]
    for i in range(n):
        factor = primefactor(arr[i])
        if factor in fact:
            bisect.insort(stack, fact[factor] + 1)
        fact[factor] = i

        for j in range(k + 1):
            if j < len(stack):
                left[i][j] = stack[-j - 1]

    for i in range(n):
        for j in range(k + 1):
            for t in range(j + 1):
                l = left[i][t]
                if l > 0:
                    dp[i][j] = min(dp[l - 1][j - t] + 1, dp[i][j])
                else:
                    dp[i][j] = 1
    return dp[-1][-1]


def main(n):
    """
    n: 问题规模，用于生成测试数据。
       这里令数组长度 = n，k 也与 n 相关。
    """
    random.seed(0)

    # 生成测试用例数量
    T = 1

    results = []
    for _ in range(T):
        # 根据 n 生成 k 和数组长度
        length = n
        k = max(0, min(20, n // 5))  # 控制 k 不过大

        # 生成数组数据，元素取值控制在一定范围内，保证有足够的质因数
        arr = [random.randint(1, 2000) for _ in range(length)]

        ans = solve_single_case(length, k, arr)
        results.append(ans)

    # 按原程序行为只打印答案（多测试用例则多行）
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)