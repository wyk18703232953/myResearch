import sys
input = sys.stdin.readline

n = int(input())
mod = pow(10, 9) + 7
a = list(map(int, input().split()))
l = 100000
cnt = [0] * (l + 1)
for i in a:
    cnt[i] += 1
pow2 = [1]
for _ in range(l):
    pow2.append(2 * pow2[-1] % mod)
ans = pow2[n] - 1
x = [-1] * (l + 1)
for i in range(2, l + 1):
    c = cnt[i]
    xi = x[i]
    for j in range(2 * i, l + 1, i):
        c += cnt[j]
        x[j] -= xi
    ans += xi * (pow2[c] - 1) % mod
    ans %= mod
print(ans)