import sys,os,io,time,copy,math
from functools import lru_cache
if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')  


def main():  
    n,k=map(int,input().split())
    arr=[]
    for i in range(n):
        x,y=map(int,input().split())
        arr.append((x,y))
        arr.sort(key=lambda x:(x[0],-x[1]),reverse=True)
    req=arr[k-1]
    count=0
    for a in arr:
        if a==req:
            count+=1
    print(count)

main()
    