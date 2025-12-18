import sys
import math
import collections
import bisect
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
for t in range(1):
    n=int(input())
    string=[]
    for i in range(100):
        string.append([])
    for i in range(n):
        val=((get_string()))
        size=len(val)
        string[size-1].append(val)
    for i in range(100):
        if len(string[i])>0:
            string[i].sort()
    ans=[]
    poss=True
    for i in range(100):
        if len(string[i])==0:
            continue
        else:
            row=string[i]
            if len(set(row))>1:
                poss=False
    if poss==False:
        print("NO")
    else:
        for i in range(100):
            if len(string[i])==0:
                continue
            for j in range(i+1,100):
                if len((string[j]))==0:
                    continue
                sub_string=(string[i][0])
                main=(string[j][0])
                if sub_string in main:
                    res=True
                else:
                    res=False
                if res==False:
                    poss=False
                    break
                else:
                    break
        if poss==False:
            print("NO")
        else:
            print("YES")
            for i in range(100):
                if len(string[i])==0:
                    continue
                for j in range(len(string[i])):
                    print(string[i][j])