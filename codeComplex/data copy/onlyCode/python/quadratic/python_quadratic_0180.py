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
mod = 998244353;
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
    if r == 0: return 1;
    return ((f[n]*inverseMod(f[n-r],m))%m*inverseMod(f[r],m))%m;

def main():
    B();

dp = [];
def D():
    [n,k] = ti();
    a = ti();
    a = sorted(a);
    cnt = [0 for i in range(n)];
    for i in range(n):
        c = 0;
        for j in range(i,n):
            if a[j]-a[i] <= 5: c+=1;
            else:break;
        cnt[i] = c;
     
    global dp;
    dp = [[0 for j in range(k+1)] for i in range(n+1)];
    ans = 0;
    for i in range(n):
        for j in range(k+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]);
            if j+1 <= k:
                dp[i+cnt[i]][j+1] = max(dp[i+cnt[i]][j+1], dp[i][j]+cnt[i]);
    print(dp[n][k]);

def B():
    n = pi();
    a = ti();
    q = pi();

    mat = [[0 for j in range(n)] for i in range(n)];
    dp = [[0 for i in range(n)] for j in range(n)];
    for i in range(n):
        for j in range(n):
            if i == j:
                mat[i][j] = a[i];
                dp[i][j] = a[i];
    i = 0;
    x = 1;
    while x < n:
        j = x;
        i = 0;
        while j < n:
            mat[i][j] = mat[i][j-1] ^ mat[i+1][j];
            j += 1;
            i += 1;
        x += 1;
    
    i = 0;
    x = 1;
    while x < n:
        j = x;
        i = 0;
        while j < n:
            dp[i][j] = max(mat[i][j], dp[i][j-1], dp[i+1][j]);
            j += 1;
            i += 1;
        x += 1;
        
    for i in range(q):
        [l,r] = ti();
        print(dp[l-1][r-1]);

            


main();