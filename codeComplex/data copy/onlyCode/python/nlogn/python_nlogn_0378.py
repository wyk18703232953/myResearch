from sys import stdin, stdout
from collections import defaultdict, Counter, deque
for _ in range(1):
    n,k=map(int, stdin.readline().split())
    li = list(map(int, stdin.readline().split()))
    dic=Counter(li)
    li=list(set(li))
    li.sort()
    n=len(li)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if li[j]+k>=li[i] and dic[li[j]]!=0:
                dic[li[j]]=0
            else:
                break
    stdout.write(str(sum(dic.values()))+"\n")