import bisect

# 预计算素数
prime = [2]
for i in range(3, 4 * 10 ** 3, 2):
    if i % 2 == 0:
        continue
    flag = False
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
            num = num // prime[index]
            times += 1
        if times & 1:
            output.append(prime[index])
        index += 1
    if num > 1:
        output.append(num)
    return tuple(output)


def solve_one(n, k, arr):
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

    # DP 计算
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
    n 为数组规模。
    本函数内部根据 n 生成测试数据，并调用原逻辑进行计算。
    返回结果值。
    """
    # 生成测试数据示例：
    # k 取一个与 n 相关的值，这里取 k = min(10, n)
    k = min(10, n)

    # arr 元素取 1..2000 范围内的数，避免超出预处理素数范围
    # 简单构造：重复模式保证有一些重复 primefactor
    arr = [(i * 37) % 2000 + 1 for i in range(1, n + 1)]

    # 调用一次原算法
    result = solve_one(n, k, arr)
    # print(result)
    pass
    return result