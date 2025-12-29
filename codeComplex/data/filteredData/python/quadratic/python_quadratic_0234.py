import random

def solve(N, S, C):
    dp = [float('inf')] * N
    for i in range(1, N):
        for j in range(i):
            if S[j] < S[i]:
                dp[i] = min(dp[i], C[j] + C[i])

    dp2 = [float('inf')] * N
    for i in range(N - 1, 0, -1):
        for j in range(i + 1, N, 1):
            if S[i] < S[j]:
                dp2[j] = min(dp2[j], dp[i] + C[j])

    ans = min(dp2)
    if ans == float('inf'):
        return -1
    return ans


def main(n):
    # 根据 n 生成测试数据
    N = n
    # 生成 S 为 1..10^6 范围内的随机整数
    S = [random.randint(1, 10**6) for _ in range(N)]
    # 生成 C 为 1..10^6 范围内的随机花费
    C = [random.randint(1, 10**6) for _ in range(N)]

    result = solve(N, S, C)
    print(result)


if __name__ == "__main__":
    # 你可以在这里指定规模进行简单测试
    main(5)