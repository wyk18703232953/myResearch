from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]

r, g, b = rints()
ar, ag, ab = [sorted(rints(), reverse=True) for _ in range(3)]
mem = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
ans = 0

for r1 in range(r + 1):
    for g1 in range(g + 1):
        for b1 in range(b + 1):
            if r1 < r:
                if g1 < g:
                    mem[r1 + 1][g1 + 1][b1] = max(mem[r1 + 1][g1 + 1][b1], (ar[r1] * ag[g1]) + mem[r1][g1][b1])
                if b1 < b:
                    mem[r1 + 1][g1][b1 + 1] = max(mem[r1 + 1][g1][b1 + 1], (ar[r1] * ab[b1]) + mem[r1][g1][b1])

            if g1 < g and b1 < b:
                mem[r1][g1 + 1][b1 + 1] = max(mem[r1][g1 + 1][b1 + 1], (ag[g1] * ab[b1]) + mem[r1][g1][b1])

            ans = max(ans, mem[r1][g1][b1])

print(ans)