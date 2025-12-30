import random

def main(n: int) -> int:
    # 1. 根据规模 n 生成 R, G, B
    #   这里简单设定：R = G = B = n
    #   如需其他方式，可按需修改
    R = G = B = n

    # 2. 生成测试数据 L
    #   L 为 3 个颜色数组，每个数组长度分别为 R, G, B
    #   使用 1~100 的随机整数并排序，以保持与原代码中 sorted(...) 一致
    L = [
        sorted(random.randint(1, 100) for _ in range(R)),
        sorted(random.randint(1, 100) for _ in range(G)),
        sorted(random.randint(1, 100) for _ in range(B)),
    ]

    # 3. 原逻辑：三维 DP 压成一维
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
                        best = max(
                            best,
                            L[0][r - 1] * L[2][b - 1] + DP[idx(r - 1, g, b - 1)],
                        )

                if g and b:
                    best = max(
                        best,
                        L[1][g - 1] * L[2][b - 1] + DP[idx(r, g - 1, b - 1)],
                    )

                DP[idx(r, g, b)] = best

    ans = max(DP)
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)