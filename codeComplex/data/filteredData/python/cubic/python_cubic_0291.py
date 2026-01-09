def main(n):
    # Interpret n as base size for r, g, b
    # Keep them balanced so the 3D DP doesn't explode too fast
    if n <= 0:
        # print(0)
        pass
        return

    # Example mapping; still deterministic and scalable
    r = n
    g = max(1, n // 2)
    b = max(1, (n + 1) // 2)

    # Deterministic generation of arrays, then sort in reverse as original
    ar = sorted([i * 2 + 1 for i in range(r)], reverse=True)
    ag = sorted([i * 3 + 2 for i in range(g)], reverse=True)
    ab = sorted([i * 5 + 3 for i in range(b)], reverse=True)

    mem = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0

    for r1 in range(r + 1):
        for g1 in range(g + 1):
            for b1 in range(b + 1):
                cur = mem[r1][g1][b1]
                if r1 < r:
                    if g1 < g:
                        val = ar[r1] * ag[g1] + cur
                        if val > mem[r1 + 1][g1 + 1][b1]:
                            mem[r1 + 1][g1 + 1][b1] = val
                    if b1 < b:
                        val = ar[r1] * ab[b1] + cur
                        if val > mem[r1 + 1][g1][b1 + 1]:
                            mem[r1 + 1][g1][b1 + 1] = val
                if g1 < g and b1 < b:
                    val = ag[g1] * ab[b1] + cur
                    if val > mem[r1][g1 + 1][b1 + 1]:
                        mem[r1][g1 + 1][b1 + 1] = val
                if cur > ans:
                    ans = cur

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)