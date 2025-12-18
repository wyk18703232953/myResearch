# CLONED CPP SOLUTION
def rr(): return input().rstrip()
def rri(): return int(rr())
def rrm(): return list(map(int, rr().split()))
from collections import defaultdict
def mus(d=0): return defaultdict(defaultdict(d))
def ms(x, y, d=0): return [[d]*y for i in range(x)]
def ar(x, d=0): return [d]*x
def ppm(m, n=0, x=0, y=0): print("\n".join(("\t".join((str(m[j][i]) for j in range(y or n))) for i in range(x or n))))
def ppa(a, n): print("\t".join(map(str, a[0:n])))
def ppl(): print("\n+"+"- -"*20+"+\n")
INF = float("inf")

def fake_input():
    return ...

# Globals
dp = ms(501, 501)
dp2 = ar(501, INF)

def read():
    n = rri()
    global arr
    arr = rrm()
    return arr, n


def calc_dp(l, r):
    assert l < r

    if l+1 == r:
        dp[l][r] = arr[l]
        return dp[l][r]
    if dp[l][r] != 0:
        return dp[l][r]

    dp[l][r] = -1

    for i in range(l+1, r):
        lf = calc_dp(l, i)
        rg = calc_dp(i, r)
        if (lf > 0 and lf == rg):
            dp[l][r] = lf + 1
            return dp[l][r]

    return dp[l][r]

def solve(arr, n):
    dp2[0] = 0

    for i in range(n):
        for j in range(i+1, n+1):
            v = calc_dp(i, j)
            #print(f"v:{v}, i:{i}, j:{j}")
            if (v > 0):
                dp2[j] = min(dp2[j], dp2[i]+1)
            #ppm(dp, 9)
            #pl()

    ans = dp2[n]
    return ans

if __name__ == "__main__":
    #input_data = fake_input()
    input_data = read()

    result = solve(*input_data)
    print(result)
