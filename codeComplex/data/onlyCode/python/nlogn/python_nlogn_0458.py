import sys
import math
import collections
import bisect
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
for t in range(1):
    n,k=get_ints()
    arr=get_list()
    ans=arr.copy()
    ans.sort(reverse=True)
    ans=ans[:k]
    c=k
    print(sum(ans))
    j = 0
    for i in range(n):
        if (arr[i] in ans and c != 1):
            print(i + 1 - j, end=' ')
            j = i + 1
            ans.remove(arr[i])
            c -= 1
        if (c == 1):
            print(n - j)
            break