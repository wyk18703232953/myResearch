from itertools import chain, combinations
from random import randint
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

n,l,r,x=map(int,input().split())
ll=list(map(int,input().split()))
subsets=powerset(ll)
res=0
for i in subsets:
    if len(i) >= 2 and l<= sum(i) <=r and max(i)-min(i) >= x:
        res+=1
print(res)
