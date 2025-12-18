def sum_of_digits(n):
    ans = 0
    while(n):
        ans += n%10
        n//=10
    return ans

n,s = map(int,input().split())
lo = 0; hi = n
x = n+1
while(lo<=hi):
    mid = (lo+hi)//2
    if(mid - sum_of_digits(mid) >= s):
        x = min(mid,x)
        hi = mid - 1
    else:
        lo = mid + 1
print(n - x + 1)