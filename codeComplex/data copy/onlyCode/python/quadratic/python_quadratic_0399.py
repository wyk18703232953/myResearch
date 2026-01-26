import sys
import math
from collections import defaultdict,deque

input = sys.stdin.readline
def inar():
    return [int(el) for el in input().split()]
def main():
    n,k=inar()
    st=input().strip()
    res=st
    pos=1
    cnt=1
    while cnt<k:
        suffix=0
        counter=0
        for i in range(pos,len(res)):
            if res[i]==st[suffix]:
                suffix+=1
            else:
                counter=1
                break
        if counter:
            pos+=1
            continue
        if pos>len(res):
            res+=st
            cnt+=1
            pos+=1
            continue
        res+=st[suffix:n]
        cnt+=1
        pos+=1
    print(res)




if __name__ == '__main__':
    main()



