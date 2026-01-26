import sys
import math
import collections
import bisect
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
for t in range(1):
    n=int(input())
    starting=[]
    ending=[]
    points=[]
    for i in range(n):
        x,y=get_ints()
        starting.append(x)
        ending.append(y)
    ans=0
    start_count=collections.Counter(starting)
    end_count=collections.Counter(ending)
    s=starting.copy()
    s.sort()
    e=ending.copy()
    e.sort()
    maxim=max(starting)
    minim=min(ending)
    #print(maxim,minim)
    for i in range(n):
        if starting[i]==maxim:
            if start_count[maxim]>1:
                loc_max=maxim
            else:
                pos=bisect.bisect_left(s,maxim)
                loc_max=s[pos-1]
        else:
            loc_max=maxim
        if ending[i]==minim:
            if end_count[minim]>1:
                loc_min=minim
            else:
                pos=bisect.bisect_right(e,minim)
                loc_min=e[pos]
        else:
            loc_min=minim
        ans=max(ans,loc_min-loc_max)
        #print(loc_max,loc_min)
    print(ans)