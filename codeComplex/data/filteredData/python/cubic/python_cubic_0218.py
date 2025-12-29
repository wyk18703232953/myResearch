import random

def main(n: int):
    # 规模约束：三维DP数组每维最多 200（原代码最大到 201）
    # 这里将 n 视为总规模，平均分配给 n, m, q
    total = min(n, 200 * 3)  # 防止过大
    base = total // 3
    rem = total % 3

    # 分配 n, m, q，使 n + m + q ≈ n，且每个不超过 200
    na = min(base + (1 if rem > 0 else 0), 200)
    mb = min(base + (1 if rem > 1 else 0), 200)
    qc = min(total - na - mb, 200)
    if qc < 0:
        qc = 0

    # 生成测试数据：随机正整数，保证非空时有值
    random.seed(0)
    a = sorted([random.randint(1, 1000) for _ in range(na)], reverse=True)
    b = sorted([random.randint(1, 1000) for _ in range(mb)], reverse=True)
    c = sorted([random.randint(1, 1000) for _ in range(qc)], reverse=True)

    # 初始化 DP，维度固定为 201，和原程序一致
    MAXL = 201
    dp = [[[0] * MAXL for _ in range(MAXL)] for _ in range(MAXL)]

    # 原始 DP 逻辑
    for ijk in range(na + mb + qc + 1):
        # i: 使用了 a 中的多少个
        for i in range(min(na + 1, ijk + 1)):
            # j: 使用了 b 中的多少个
            max_j = min(mb + 1, ijk - i + 1)
            for j in range(max_j):
                k = ijk - i - j
                if k < 0 or k > qc:
                    continue

                cur = dp[i][j][k]

                # 跳过一个 a
                if i + 1 <= na:
                    if dp[i + 1][j][k] < cur:
                        dp[i + 1][j][k] = cur

                # 跳过一个 b
                if j + 1 <= mb:
                    if dp[i][j + 1][k] < cur:
                        dp[i][j + 1][k] = cur

                # 跳过一个 c
                if k + 1 <= qc:
                    if dp[i][j][k + 1] < cur:
                        dp[i][j][k + 1] = cur

                # 匹配 a[i] 和 b[j]
                if i + 1 <= na and j + 1 <= mb:
                    val = cur + a[i] * b[j]
                    if dp[i + 1][j + 1][k] < val:
                        dp[i + 1][j + 1][k] = val

                # 匹配 a[i] 和 c[k]
                if i + 1 <= na and k + 1 <= qc:
                    val = cur + a[i] * c[k]
                    if dp[i + 1][j][k + 1] < val:
                        dp[i + 1][j][k + 1] = val

                # 匹配 b[j] 和 c[k]
                if j + 1 <= mb and k + 1 <= qc:
                    val = cur + b[j] * c[k]
                    if dp[i][j + 1][k + 1] < val:
                        dp[i][j + 1][k + 1] = val

    print(dp[na][mb][qc])

if __name__ == "__main__":
    # 示例调用：规模参数可调
    main(60)