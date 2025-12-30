import bisect
import random

# 预处理素数
prime = [2]
for i in range(3, 4 * 10 ** 3, 2):
    flag = False
    if i % 2 == 0:
        continue
    for j in range(3, int(i ** 0.5) + 1, 2):
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


def solve_one_case(n, k, arr):
    fact = {}
    left = [[0] * (k + 1) for _ in range(n)]
    dp = [[300000] * (k + 1) for _ in range(n)]

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
    # n 作为规模参数，生成测试数据
    # 可以根据需要调整 k 和 arr 的生成策略
    random.seed(0)
    T = 1
    k = min(5, n)  # 示例：k 不超过 5
    # 生成正整数数组，保证不为 0
    arr = [random.randint(1, 10 ** 6) for _ in range(n)]

    # 只处理一个测试用例，返回/打印结果
    ans = solve_one_case(n, k, arr)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n=10
    main(10)