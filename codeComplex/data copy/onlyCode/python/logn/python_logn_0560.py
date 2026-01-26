#Bhargey Mehta (Junior)
#DA-IICT, Gandhinagar
import sys, math, queue, bisect
#sys.stdin = open('input.txt', 'r')
MOD = 998244353
sys.setrecursionlimit(1000000)

n = int(input())
if n < 10:
    print(n)
    exit()
d = 1
while n > 9*d*pow(10, d-1):
    n -= 9*d*pow(10, d-1)
    d += 1
x = pow(10, d-1) + (n-1)//d
p = n % d
x = str(x).zfill(d)
print(x[p-1])