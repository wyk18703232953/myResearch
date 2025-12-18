import sys
import math
import collections
import bisect
import string
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
for t in range(1):
    n=int(input())
    s1=list(get_string())
    s2=list(get_string())
    count=0
    ans=[]
    lower=string.ascii_lowercase
    np=0
    for i in lower:
        if s1.count(i)!=s2.count(i):
            np+=1
            break
    if np>0:
        print(-1)
        continue
    pos=dict()
    for i in range(n):
        if s1[i] in pos:
            pos[s1[i]].append(i)
        else:
            pos[s1[i]]=[i]
    for i in range(n):
        if s1[i]==s2[i]:
            continue
        else:
            row=pos[s2[i]]
            no=0
            for j in range(len(row)):
                if row[j]>i:
                    no=row[j]
                    break
            for j in range(no,i,-1):
                ans.append(j)
            s1.pop(no)
            s1.insert(i,s2[i])
            #print(s1)
            pos = dict()
            for j in range(n):
                if s1[j] in pos:
                    pos[s1[j]].append(j)
                else:
                    pos[s1[j]] = [j]
    print(len(ans))
    print(*ans)