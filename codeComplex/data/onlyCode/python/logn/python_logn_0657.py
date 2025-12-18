from sys import stdin
#####################################################################
def iinput(): return int(stdin.readline())
def minput(): return map(int, stdin.readline().split())
def linput(): return list(map(int, stdin.readline().split()))
#####################################################################

n, k = minput()
l, r = 0, n
while l<r:
    mid = (l+r)//2
    if ((n-mid)*(n-mid+1))//2 - mid == k:
        print(mid)
        break
    elif ((n-mid)*(n-mid+1))//2 - mid > k:
        l = mid
    else:
        r = mid
