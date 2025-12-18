#!/usr/bin/python3
#Businessmen Problems
ans={}
for _ in range(int(input())):
    a,b=map(int,input().split())
    ans[a]=b
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a in ans:
        ans[a]=max(ans[a],b)
    else:
        ans[a]=b
print(sum(ans.values()))
