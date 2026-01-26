import bisect
import copy
import decimal
import fractions
import heapq
import itertools
import math
import random
import sys
from collections import Counter,deque,defaultdict
from functools import lru_cache,reduce
from heapq import heappush,heappop,heapify,heappushpop,_heappop_max,_heapify_max
def _heappush_max(heap,item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)
def _heappushpop_max(heap, item):
    if heap and item < heap[0]:
        item, heap[0] = heap[0], item
        heapq._siftup_max(heap, 0)
    return item
from math import gcd as GCD
read=sys.stdin.read
readline=sys.stdin.readline
readlines=sys.stdin.readlines

class Prime:
    def __init__(self,N):
        assert N<=10**8
        self.smallest_prime_factor=[None]*(N+1)
        for i in range(2,N+1,2):
            self.smallest_prime_factor[i]=2
        n=int(N**.5)+1
        for p in range(3,n,2):
            if self.smallest_prime_factor[p]==None:
                self.smallest_prime_factor[p]=p
                for i in range(p**2,N+1,2*p):
                    if self.smallest_prime_factor[i]==None:
                        self.smallest_prime_factor[i]=p
        for p in range(n,N+1):
            if self.smallest_prime_factor[p]==None:
                self.smallest_prime_factor[p]=p
        self.primes=[p for p in range(N+1) if p==self.smallest_prime_factor[p]]

    def Factorize(self,N):
        assert N>=1
        factorize=defaultdict(int)
        if N<=len(self.smallest_prime_factor)-1:
            while N!=1:
                factorize[self.smallest_prime_factor[N]]+=1
                N//=self.smallest_prime_factor[N]
        else:
            for p in self.primes:
                while N%p==0:
                    N//=p
                    factorize[p]+=1
                if N<p*p:
                    if N!=1:
                        factorize[N]+=1
                    break
                if N<=len(self.smallest_prime_factor)-1:
                    while N!=1:
                        factorize[self.smallest_prime_factor[N]]+=1
                        N//=self.smallest_prime_factor[N]
                    break
            else:
                if N!=1:
                    factorize[N]+=1
        return factorize

    def Divisors(self,N):
        assert N>0
        divisors=[1]
        for p,e in self.Factorize(N).items():
            A=[1]
            for _ in range(e):
                A.append(A[-1]*p)
            divisors=[i*j for i in divisors for j in A]
        return divisors

    def Is_Prime(self,N):
        return N==self.smallest_prime_factor[N]

    def Totient(self,N):
        for p in self.Factorize(N).keys():
            N*=p-1
            N//=p
        return N

    def Mebius(self,N):
        fact=self.Factorize(N)
        for e in fact.values():
            if e>=2:
                return 0
        else:
            if len(fact)%2==0:
                return 1
            else:
                return -1

N=int(readline())
A=list(map(int,readline().split()))
mod=10**9+7
m=max(A)
cnt=[0]*(m+1)
P=Prime(m)
for a,c in Counter(A).items():
    cnt[a]=c
for p in P.primes:
    for i in range(m//p,0,-1):
        cnt[i]+=cnt[i*p]
for i in range(1,m+1):
    cnt[i]=pow(2,cnt[i],mod)-1
    cnt[i]%=mod
for p in P.primes:
    for i in range(p,m+1,p):
        cnt[i//p]-=cnt[i]
        cnt[i//p]%=mod
ans=cnt[1]
print(ans)