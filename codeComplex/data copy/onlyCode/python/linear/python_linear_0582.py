def init_input():
    import os
    from sys import stdin
    it = iter(os.read(stdin.fileno(), 10 ** 7).split())
    return lambda: next(it).decode(), lambda: int(next(it)), lambda: float(next(it))
ns, ni, nf = init_input()

MOD = 10 ** 9 + 7

n, q = ni(), ni()
s = 'x' + ns()
c = [0] * (n + 1)
for i in range(1, n + 1):
    c[i] = c[i - 1] + (s[i] == '1')

p2 = [1] * (2 * n + 1)
for i in range(1, 2 * n + 1):
    p2[i] = p2[i - 1] * 2 % MOD

out = []
for qq in range(q):
    l, r = ni(), ni()
    o = c[r] - c[l - 1]
    z = (r - l + 1) - o
    ans = (p2[o + z] - 1 - p2[z] + 1) % MOD
    out.append(ans)
print(*out, sep='\n')
