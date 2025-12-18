# sys.setrecursionlimit(300000)
import sys
def main():
    pass
def binary(n):
    # decimal to binary
    return (bin(n).replace("0b", ""))
def decimal(s):
    # binary to decimal
    return (int(s, 2))
def pow2(n):
    # power of a number base 2
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return (p)
def isPrime(n):
    # if  number is prime in √n time
    if (n == 1):
        return (False)
    else:
        root = int(n ** 0.5)
        root += 1
        for i in range(2, root):
            if (n % i == 0):
                return (False)
        return (True)
def lts(l):
    # list to string ,no spaces
    s = ''.join(map(str, l))
    return s
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
# 1000000007
mod = int(1e9) + 7
def ssinp(): return sys.stdin.readline().strip()
#s=input()
def iinp(): return int(input())
#n=int(input())
def nninp(): return map(int, sys.stdin.readline().strip().split())
#n, m, a=[int(x) for x in input().split()]
def llinp(): return list(map(int, sys.stdin.readline().strip().split()))
#a=list(map(int,input().split()))
def p(xyz): print(xyz)
def p2(a, b): print(a, b)
import math
from collections import OrderedDict
from fractions import Fraction
#for _ in range(iinp()):
n,m=nninp()
x=llinp()
y=llinp()
for c in x:
    if(c in y):
        print(c,end=" ")



