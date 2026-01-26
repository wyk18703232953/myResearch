import itertools

n = int(input())
a = []
for i in range(4):
    a.append([input() for _ in range(n)])
    if i < 3:
        assert input() == ''

best = 4*n*n
for p in itertools.permutations(a):
    for s in range(2):
        count = 0
        for i in range(4):
            for r in range(n):
                for c in range(n):
                    if p[i][r][c] != str((s + (i//2 + r) + (i % 2 + c)) % 2):
                        count += 1
        best = min(best, count)
print(best)
