import bisect

# 预处理素数
prime = [2]
for i in range(3, 4 * 10**3, 2):
    flag = False
    if i % 2 == 0:
        continue
    for j in range(3, int(i**0.5) + 1, 2):
        if i % j == 0:
            flag = True
            break
    if not flag:
        prime.append(i)


def primefactor(num):
    index = 0
    output = []

    while num >= prime[index] ** 2:
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


def solve_case(n, k, arr):
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
    n: 问题规模，用作数组长度。
    这里根据 n 生成一组测试数据：
      - k 设为 20，若 n 较小则取较小值
      - arr 生成为 [i+1 for i in range(n)]
    返回算法结果（原程序最后输出的值）。
    """
    # 可按需要调整生成方式
    k = min(20, n)  # 控制 k 不大于 n
    arr = [i + 1 for i in range(n)]
    return solve_case(n, k, arr)


if __name__ == "__main__":
    # 示例：调用 main(100)
    result = main(100)
    # print(result)
    pass