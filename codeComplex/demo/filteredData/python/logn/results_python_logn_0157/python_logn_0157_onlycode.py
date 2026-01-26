import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def sum(n,r):
    return n*(2*r - (n-1))//2

def function(total, l, r):
    left = l
    right = r

    while left<=right:
        mid = (right + left) // 2
        result = sum(r-mid+1, r)
        if result==total:
            return r-mid+1
        elif result > total:
            left = mid + 1
        else:
            if sum(r-mid+2,r) > total:
                return r-mid + 2
            else:
                right = mid - 1
    return -1


n, m = multi_input()

n = n-1
m = m-1
if n==0:
    print(0)
elif sum(m,m)<n:
    print(-1)
elif m<n:
    print(function(n, 1, m))
else:
    print(1)
