import sys
input = lambda : sys.stdin.readline().rstrip()


sys.setrecursionlimit(2*10**5+10)
write = lambda x: sys.stdout.write(x+"\n")
debug = lambda x: sys.stderr.write(x+"\n")
writef = lambda x: print("{:.12f}".format(x))


# zeta mebius
def zeta_super(val, n):
    # len(val)==2^n
    out = val[:]
    for i in range(n):
        for j in range(1<<n):
            if not j>>i&1:
                out[j] += out[j^(1<<i)]
    return out

n = int(input())
a = list(map(int, input().split()))
m = max(a).bit_length()
M = 10**9+7
v = [0]*(1<<m)
for item in a:
    v[item] += 1
v2 = [1]
for i in range(n+1):
    v2.append(v2[-1]*2%M)
nv = zeta_super(v, m)
ans = 0
for b in range(1<<m):
    ans += (v2[nv[b]]-1)*pow(-1, bin(b).count("1"))
    ans %= M
print(ans%M)