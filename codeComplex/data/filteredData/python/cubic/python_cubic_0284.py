import random

def solve(dp, r, g, b, R, G, B, ra, ga, ba):
    if dp[r][g][b] != -1:
        return dp[r][g][b]

    count = 0
    for i, j in zip((r, g, b), (R, G, B)):
        if i == j:
            count += 1
    if count >= 2:
        return 0

    res = -10**18

    if r != R and b != B:
        res = max(res, ra[r] * ba[b] + solve(dp, r + 1, g, b + 1, R, G, B, ra, ga, ba))

    if r != R and g != G:
        res = max(res, ra[r] * ga[g] + solve(dp, r + 1, g + 1, b, R, G, B, ra, ga, ba))

    if b != B and g != G:
        res = max(res, ba[b] * ga[g] + solve(dp, r, g + 1, b + 1, R, G, B, ra, ga, ba))

    dp[r][g][b] = res
    return res


def main(n):
    # 根据规模 n 生成 R, G, B（不超过 200，防止越界）
    R = min(n, 200)
    G = min(max(n - 1, 1), 200)
    B = min(max(n - 2, 1), 200)

    # 生成测试数据：随机正整数
    random.seed(0)
    ra = [random.randint(1, 1000) for _ in range(R)]
    ga = [random.randint(1, 1000) for _ in range(G)]
    ba = [random.randint(1, 1000) for _ in range(B)]

    ra.sort(reverse=True)
    ga.sort(reverse=True)
    ba.sort(reverse=True)

    # dp 维度固定为 201，与原程序一致
    dp = [[[-1 for _ in range(201)] for _ in range(201)] for _ in range(201)]

    ans = solve(dp, 0, 0, 0, R, G, B, ra, ga, ba)
    print(ans)


# 示例运行
if __name__ == "__main__":
    main(10)