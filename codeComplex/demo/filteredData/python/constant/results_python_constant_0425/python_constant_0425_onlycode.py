import sys
# Get out of main functoin
def main():
    pass
# decimal to binary
def binary(n):
    return (bin(n).replace("0b", ""))
# binary to decimal
def decimal(s):
    return (int(s, 2))
# power of a number base 2
def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return (p)
# if  number is prime in √n time
def isPrime(n):
    if (n == 1):
        return (False)
    else:
        root = int(n ** 0.5)
        root += 1
        for i in range(2, root):
            if (n % i == 0):
                return (False)
        return (True)
# list to string ,no spaces
def lts(l):
    s = ''.join(map(str, l))
    return s
# String to list
def stl(s):
    # for each character in string to list with no spaces -->
    l = list(s)
    # for space in string  -->
    # l=list(s.split(" "))
    return l
# Returns list of numbers with a particular sum
def sq(a, target, arr=[]):
    s = sum(arr)
    if (s == target):
        return arr
    if (s >= target):
        return
    for i in range(len(a)):
        n = a[i]
        remaining = a[i + 1:]
        ans = sq(remaining, target, arr + [n])
        if (ans):
            return ans
# Sieve for prime numbers in a range
def SieveOfEratosthenes(n):
    cnt = 0
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            cnt += 1
            # print(p)
    return (cnt)
# for positive integerse only
def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)
# 1000000007
mod = int(1e9) + 7
def ssinp(): return sys.stdin.readline().strip()
# s=input()
def iinp(): return int(input())
# n=int(input())
def nninp(): return map(int, sys.stdin.readline().strip().split())
# n, m, a=[int(x) for x in input().split()]
def llinp(): return list(map(int, sys.stdin.readline().strip().split()))
# a=list(map(int,input().split()))
def p(xyz): print(xyz)
def p2(a, b): print(a, b)
import math
#import random
#sys.setrecursionlimit(300000)
#from fractions import Fraction
#from collections import OrderedDict
#from collections import deque
########################                         list.sort(key=lambda x:x[1]) for sorting a list according to second element in sublist            ########################
########################                         Speed: STRING < LIST < SET,DICTIONARY                      ########################
########################                         from collections import deque                              ########################
########################                         ASCII of A-Z= 65-90                                        ########################
########################                         ASCII of a-z= 97-122                                       ########################
########################                         d1.setdefault(key, []).append(value)                       ########################
#for __ in range(iinp()):
n,k=nninp()
if(k>=2*n):
    p(0)
elif(k<=n):
    if(k%2==1):
        p(k//2)
    else:
        p(k//2-1)
else:
    if(k%2==1):
       print(k//2-(k-n)+1)
    else:
        print(k//2 - (k - n))









