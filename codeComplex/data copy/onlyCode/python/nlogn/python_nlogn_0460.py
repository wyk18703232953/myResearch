import sys
import math
from collections import defaultdict,deque

input = sys.stdin.readline
def inar():
    return [int(el) for el in input().split()]
def main():
    n,k=inar()
    arr=inar()
    new=arr.copy()
    new=[]
    ans=0
    for i in range(n):
        new.append((arr[i],i))
    new.sort(reverse=True)
    check=[0]*n
    for i in range(k):
        ans+=new[i][0]
        check[new[i][1]]=1
    count=0
    res=[]
    #print(check)
    for i in range(n):
        if check[i]==1:
            count+=1
            res.append(count)
            count=0
        else:
            count+=1
    res[-1]+=count
    print(ans)
    print(*res)




if __name__ == '__main__':
    main()



