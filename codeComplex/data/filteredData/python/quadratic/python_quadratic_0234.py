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
    # n 表示 N（序列长度）
    if n <= 0:
        return

    N = n
    # 确定性构造 S 和 C
    # S 为一个有规律的整数序列，包含一些重复和递增模式
    S = [(i * 3 + (i // 2)) % (n + 7) for i in range(N)]
    # C 为正成本，随位置线性变化
    C = [(i * 2 + 1) for i in range(N)]

    result = solve(N, S, C)
    print(result)


if __name__ == "__main__":
    # 示例调用，可自行修改 n 的大小做时间复杂度实验
    main(10)