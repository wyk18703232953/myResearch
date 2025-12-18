def arr_inp():
    return [int(x) for x in stdin.readline().split()]


def nCr(n, r):
    f, m = factorial, 1
    for i in range(n, n - r, -1):
        m *= i
    return int(m // f(r))


from math import factorial
from sys import stdin

n, a, ans, tem = int(input()), arr_inp(), [], 0
mem = [0] * (n + 1)

for i in range(n):
    for j in range(a[i] - 1, 0, -1):
        if not mem[j]:
            tem += 1
    mem[a[i]] = 1

for i in range(int(input())):
    l, r = arr_inp()
    tem += nCr(r - l + 1, 2)
    ans.append('odd' if tem % 2 else 'even')

print('\n'.join(ans))
