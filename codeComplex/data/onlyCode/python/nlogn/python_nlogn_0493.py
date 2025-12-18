import sys
import math
from collections import defaultdict,deque

input = sys.stdin.readline
def inar():
    return [int(el) for el in input().split()]
def main():
    n,m=inar()
    tup=[]
    sm=0
    for i in range(n):
        a,b=inar()
        sm+=a
        diff=a-b
        tup.append([diff,a,b])
    tup.sort(reverse=True)
    ans=0
    i=0
    while sm>m and i<n:
        sm-=tup[i][1]
        sm+=tup[i][2]
        i+=1
        ans+=1
    if sm<=m:
        print(ans)
    else:
        print(-1)




if __name__ == '__main__':
    main()



