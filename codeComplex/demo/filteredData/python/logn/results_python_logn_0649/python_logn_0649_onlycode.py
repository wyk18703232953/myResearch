# https://codeforces.com/problemset/problem/1195/B

def check(mid):
    added = n - mid
    total = ((added)*(added+1))//2
    return total - mid >= k

n,k = map(int,input().split())
low = 0
high = n-1
while low < high:
    mid = (low+high+1)//2
    # print(mid)
    if check(mid):
        low = mid
    else:
        high = mid - 1
print(low)