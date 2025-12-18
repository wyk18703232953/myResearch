def solve(n, p, s):
    p.append((0, 0))
    p.sort()
    t = 0
    while p:
        x = p.pop()
        s, t = x[0], max(x[1], t + abs(s - x[0]))
    return t


n, s = [int(x) for x in input().split(' ')]
p = [tuple([int(x) for x in input().split(' ')]) for r in range(n)]

print(solve(n, p, s))