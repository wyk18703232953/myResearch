import random

def main(n):
    # 1. 生成测试数据：长度为 n 的数组 A，元素在 1..n 之间
    N = n
    if N <= 0:
        print(0)
        return

    random.seed(0)  # 固定种子便于复现
    A = [random.randint(1, N) for _ in range(N)]

    # 2. 原逻辑：区间消缩 DP
    dp = [[False for _ in range(N)] for _ in range(N)]
    for l in range(N):
        tmp = [A[l]]
        dp[l][l] = True
        for r in range(l + 1, N):
            val = A[r]
            while tmp and tmp[-1] == val:
                val = tmp[-1] + 1
                tmp.pop()
            tmp.append(val)
            if len(tmp) == 1:
                dp[l][r] = True

    res = [i for i in range(N + 1)]
    for r in range(1, N + 1):
        for l in range(1, r + 1):
            if dp[l - 1][r - 1]:
                res[r] = min(res[r], 1 + res[l - 1])

    print(res[N])


if __name__ == "__main__":
    # 示例：n = 10
    main(10)