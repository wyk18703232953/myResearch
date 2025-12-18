input()
p = list(map(int, input().split()))
x = max(p)
if p[p.index(x)] == 1:
    p[p.index(x)] = 2
else:
    p[p.index(x)] = 1
p.sort()
print(' '.join(str(i) for i in p))