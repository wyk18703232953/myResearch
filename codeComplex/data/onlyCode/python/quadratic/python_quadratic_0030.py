import sys
import math
input = sys.stdin.readline
from functools import cmp_to_key;

def pi():
    return(int(input()))
def pl():
    return(int(input(), 16))
def ti():
    return(list(map(int,input().split())))
def ts():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
mod = 1000000007;
f = [];
def fact(n,m):
    global f;
    f = [1 for i in range(n+1)];
    f[0] = 1;
    for i in range(1,n+1):
        f[i] = (f[i-1]*i)%m;

def fast_mod_exp(a,b,m):
    res = 1;
    while b > 0:
        if b & 1:
            res = (res*a)%m;
        a = (a*a)%m;
        b = b >> 1;
    return res;

def inverseMod(n,m):
    return fast_mod_exp(n,m-2,m);

def ncr(n,r,m):
    if n < 0 or r < 0 or r > n: return 0;
    if r == 0: return 1;
    return ((f[n]*inverseMod(f[n-r],m))%m*inverseMod(f[r],m))%m;

def main():
    C();

def D():
    [n,m,k] = ti();
    w = [[] for i in range(n)];
    for i in range(n):
        w[i] = ts();

    mn = [[0 for j in range(k+1)] for i in range(n+1)];
    for i in range(1,n+1):
        for j in range(k+1):
            c = 0;
            st,en = -1,-1;
            for x in range(m):
                if w[i-1][x] == '1':
                    if c == j and st == -1: st = x;
                    if c < j: c += 1;
                    if c == j: en = x;
            mn[i][j] = en-st+1 if st != -1 and en != -1 else 0;
            st,en = -1,-1;
            c = 0;
            for x in range(m-1,-1,-1):
                if w[i-1][x] == '1':
                    if c == j and st == -1: st = x;
                    if c < j: c += 1;
                    if c == j: en = x;
            if st != -1 and en != -1 >= 0:
                mn[i][j] = min(mn[i][j], st-en+1);

    dp = [[9999999999999999 for j in range(k+1)] for i in range(n+1)];
    for i in range(k+1):
        dp[0][i] = 0;
    for i in range(1,n+1):
        for j in range(k+1):
            for x in range(k+1):
                if j-x >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-x]+mn[i][x]);

    print(dp[n][k]);

def C():
    n = pi();
    s = [];
    mxI = 0;
    for i in range(n):
        c = input();
        s.append(c[:len(c)-1]);
        if s[len(s)-1] == 'f': mxI += 1;
    dp = [[0 for j in range(mxI+1)] for i in range(n)];
    dp[0][0] = 1;
    preSum = [1 for i in range(mxI+1)];
    pre = 1;
    for i in range(1,n):
        sm = 0;
        pre = 0;
        for j in range(mxI+1):
            if s[i-1] == 'f':
                dp[i][j] = dp[i-1][j-1]%mod;
            else:
                dp[i][j] = (preSum[mxI]%mod-(pre if j != 0 else 0)%mod)%mod;
            pre = preSum[j];
            preSum[j] = ((preSum[j-1] if j != 0 else 0)%mod+dp[i][j]%mod)%mod;

    print(preSum[mxI]%mod);

main();