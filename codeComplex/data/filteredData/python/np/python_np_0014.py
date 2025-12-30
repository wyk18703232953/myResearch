import random

def main(n):
    # 生成测试数据：n x n 的随机概率矩阵（0~1之间的浮点数）
    # 原题中 b[j][i] 被使用，所以不强制对角线为 0
    random.seed(0)
    b = [[random.random() for _ in range(n)] for _ in range(n)]

    ma = 1 << n
    dp = [0.0] * ma
    dp[0] = 1.0

    for mask in range(1, ma):
        l = n - bin(mask).count("1") + 1
        res = l * (l - 1) // 2
        for i in range(n):
            if mask & (1 << i):
                prev_mask = mask ^ (1 << i)
                for j in range(n):
                    if not (mask & (1 << j)):
                        dp[mask] += (dp[prev_mask] * b[j][i]) / res

    ans = []
    full_mask = ma - 1
    for i in range(n):
        ans.append(dp[full_mask ^ (1 << i)])

    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(3)，可根据需要修改 n
    main(3)