import random

def main(n: int):
    # 这里用 n 控制 r, g, b 的规模（可按需调整生成规则）
    # 示例：让 r, g, b 在 1..n 之间随机
    r = random.randint(1, n)
    g = random.randint(1, n)
    b = random.randint(1, n)

    # 生成测试数据：随机整数 1..1000
    ar = sorted([random.randint(1, 1000) for _ in range(r)], reverse=True)
    ag = sorted([random.randint(1, 1000) for _ in range(g)], reverse=True)
    ab = sorted([random.randint(1, 1000) for _ in range(b)], reverse=True)

    mem = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0

    for r1 in range(r + 1):
        for g1 in range(g + 1):
            for b1 in range(b + 1):
                if r1 < r:
                    if g1 < g:
                        mem[r1 + 1][g1 + 1][b1] = max(
                            mem[r1 + 1][g1 + 1][b1],
                            ar[r1] * ag[g1] + mem[r1][g1][b1]
                        )
                    if b1 < b:
                        mem[r1 + 1][g1][b1 + 1] = max(
                            mem[r1 + 1][g1][b1 + 1],
                            ar[r1] * ab[b1] + mem[r1][g1][b1]
                        )

                if g1 < g and b1 < b:
                    mem[r1][g1 + 1][b1 + 1] = max(
                        mem[r1][g1 + 1][b1 + 1],
                        ag[g1] * ab[b1] + mem[r1][g1][b1]
                    )

                ans = max(ans, mem[r1][g1][b1])

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(5)