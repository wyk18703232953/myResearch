import random

def dp(r1, g1, b1, r, g, b, ar, ag, ab, mem):
    if mem[r1][g1][b1] != -1:
        return mem[r1][g1][b1]

    v1, v2, v3 = 0, 0, 0

    if r1 < r:
        if g1 < g:
            v1 = (ar[r1] * ag[g1]) + dp(r1 + 1, g1 + 1, b1, r, g, b, ar, ag, ab, mem)
        if b1 < b:
            v2 = (ar[r1] * ab[b1]) + dp(r1 + 1, g1, b1 + 1, r, g, b, ar, ag, ab, mem)

    if g1 < g and b1 < b:
        v3 = (ag[g1] * ab[b1]) + dp(r1, g1 + 1, b1 + 1, r, g, b, ar, ag, ab, mem)

    mem[r1][g1][b1] = max(v1, v2, v3)
    return mem[r1][g1][b1]


def main(n):
    # 根据规模 n 生成 r, g, b（此处简单设定为不超过 n 的正整数）
    r = random.randint(1, n)
    g = random.randint(1, n)
    b = random.randint(1, n)

    # 生成测试数据：长度分别为 r, g, b 的正整数数组
    # 为了更贴近常见题目设定，限定在 [1, 1000]
    ar = sorted([random.randint(1, 1000) for _ in range(r)], reverse=True)
    ag = sorted([random.randint(1, 1000) for _ in range(g)], reverse=True)
    ab = sorted([random.randint(1, 1000) for _ in range(b)], reverse=True)

    mem = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = dp(0, 0, 0, r, g, b, ar, ag, ab, mem)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5) 生成规模大致受 5 控制的测试数据并求解
    main(5)