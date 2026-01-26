from collections import defaultdict, deque, Counter
from sys import stdin, stdout
from heapq import heappush, heappop
import math
import io
import os
import math
import bisect

#?############################################################


def isPrime(x):
    for i in range(2, x):
        if i*i > x:
            break
        if (x % i == 0):
            return False
    return True

#?############################################################


def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


#?############################################################

def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n / i
    if n > 2:
        l.append(n)
    return list(set(l))


#?############################################################

def power(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

#?############################################################


def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime


#?############################################################

def digits(n):
    c = 0
    while (n > 0):
        n //= 10
        c += 1
    return c

#?############################################################


def ceil(n, x):
    if (n % x == 0):
        return n//x
    return n//x+1

#?############################################################


def mapin():
    return map(int, input().split())

#?############################################################
def solve(final, n):
    fifi = [[final[j][i] for j in range(n)] for i in range(n)] 
 
    k = []
    for i in range(n):
        k.append(sum(final[i]))
    a = max(k)-min(k)
    
    a = a*a
    k = []
    for i in range(n):
        k.append(sum(fifi[i]))
    b = max(k)-min(k)
    
    b = b*b
    
    
    return a+b
    
    
def inte(a, b, c, d):
    a = max(a, c)
    b = min(b, d)
    
    return [a, b]

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# python3 15.py<in>op
n = int(input())
l = []
for i in range(n):
    a, b = mapin()
    l.append([a, b])
    
    
f= []
ff = []
a = 0
b = 10000000000000
f.append([a, b])
for i in range(n):
    x = inte(a, b, l[i][0], l[i][1])
    a = x[0]
    b = x[1]
    f.append([a, b])
a = 0
b = 10000000000000
ff = [[] for i in range(n)]
for i in reversed(range(n)):
    x = inte(a, b, l[i][0], l[i][1])
    a = x[0]
    b = x[1]
    ff[i] = [a, b]
ff.append([0, 100000000000000])
ans = 0  
for i in range(n):
    a = f[i]
    b = ff[i+1]
    y = inte(a[0], a[1], b[0], b[1])
    if(y[1]>= y[0]):
        ans = max(ans, y[1]-y[0])
    
    
# print(f, ff)/
print(ans)

    
    