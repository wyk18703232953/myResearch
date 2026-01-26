'''Author- Akshit Monga'''
from sys import stdin,stdout
input=stdin.readline
t=1
for _ in range(t):
    n=int(input())
    x=input()
    c=0
    ans=0
    for i in x:
        if i=='x':
            c+=1
        else:
            ans+=max(0,c-2)
            c = 0
    ans+=max(0,c-2)
    print(ans)