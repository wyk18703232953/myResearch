import sys
import math
from collections import defaultdict,deque

input = sys.stdin.readline
def inar():
    return [int(el) for el in input().split()]
def main():
    n=int(input())
    s=list(input().strip())
    t=list(input().strip())
    res=True
    ans=[]
    for i in range(n):
        if s[i]==t[i]:
            continue
        else:
            ind=-1
            for j in range(i+1,n):
                if t[i]==s[j]:
                    ind=j
                    break
            if ind==-1:
                res=False
                break
            for j in range(ind-1,i-1,-1):
                ans.append(j+1)
                s[j],s[j+1]=s[j+1],s[j]
    if res:
        print(len(ans))
        print(*ans)
    else:
        print(-1)




if __name__ == '__main__':
    main()



