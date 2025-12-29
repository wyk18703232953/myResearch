import random

def main(n):
    # 1. 根据规模 n 生成 R, G, B
    # 尝试让 R+G+B ≈ n，且都 >= 1
    if n < 3:
        n = 3
    # 简单分配：R= n//3, G= (n+1)//3, B= n - R - G
    R = n // 3
    G = (n + 1) // 3
    B = n - R - G
    if R == 0: R = 1
    if G == 0: G = 1
    if B == 0: B = 1

    # 2. 生成三组长度分别为 R, G, B 的随机正整数，并排序
    # 数值范围可按需要调整
    A = sorted(random.randint(1, 1000) for _ in range(R))
    C = sorted(random.randint(1, 1000) for _ in range(G))
    D = sorted(random.randint(1, 1000) for _ in range(B))
    L = [A, C, D]

    # 3. 原算法逻辑
    DP = [0] * ((R + 1) * (G + 1) * (B + 1))

    def idx(r, g, b):
        return r * (G + 1) * (B + 1) + g * (B + 1) + b

    for r in range(R + 1):
        for g in range(G + 1):
            for b in range(B + 1):
                best = 0
                if r:
                    if g:
                        best = L[0][r - 1] * L[1][g - 1] + DP[idx(r - 1, g - 1, b)]
                    if b:
                        best = max(best,
                                   L[0][r - 1] * L[2][b - 1] + DP[idx(r - 1, g, b - 1)])
                if g and b:
                    best = max(best,
                               L[1][g - 1] * L[2][b - 1] + DP[idx(r, g - 1, b - 1)])
                DP[idx(r, g, b)] = best

    # 4. 输出结果（可根据需要返回）
    print(max(DP))


if __name__ == "__main__":
    # 示例：用 n = 9 运行一次
    main(9)