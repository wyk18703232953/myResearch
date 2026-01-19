import bisect
import copy
import decimal
import fractions
import functools
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

N,Q=map(int,readline().split())
P=Prime(5*10**5)
mebius=[0]+[P.Mebius(i) for i in range(1,5*10**5+1)]
cnt=[0]*(5*10**5+1)
ans=0
A=list(map(int,readline().split()))
used=[False]*(N)
for _ in range(Q):
    q=int(readline())-1
    prime=list(P.Factorize(A[q]).keys())
    l=len(prime)
    for bit in range(1<<l):
        s=1
        for i in range(l):
            if bit>>i&1:
                s*=prime[i]
        if used[q]:
            cnt[s]-=1
            ans-=cnt[s]*mebius[s]
        else:
            ans+=cnt[s]*mebius[s]
            cnt[s]+=1
    if used[q]:
        used[q]=False
    else:
        used[q]=True
    print(ans)