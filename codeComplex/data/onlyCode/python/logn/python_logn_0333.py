import sys

MOD = 10**9 + 7

x,k = list(map(int,sys.stdin.readline().strip().split(' ')))

a = x*pow(2,k+1,MOD) % MOD 
b = (a - pow(2,k,MOD) + 1) % MOD
print(b if x != 0 else 0)