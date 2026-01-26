from itertools import permutations as p
rd = lambda: map(int, input())
def f(n, t):
    a = 0
    f = 1
    for i in range(n):
        for x in rd():
            if x != f:
                a += 1
            f = 1 - f
    if t < 3:
        rd()
    return a
n = int(input())
m = []
b = [-1, -1, 1, 1]
for i in range(4):
    m.append(f(n, i))
print(2 * n ** 2 + min(sum(x * y for x, y in zip(q, m)) for q in set(p(b))))
