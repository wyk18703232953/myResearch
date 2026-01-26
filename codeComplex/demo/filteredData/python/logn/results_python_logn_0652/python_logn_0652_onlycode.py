x = list(map(int, input().split()))

start = 0
end = x[0] -1

target = x[1]

ans = 0

while start<= end:

    mid = (start+end)//2
    sum = mid*(mid+1) //2

    ans1 = x[0] - mid

    if sum - ans1 == target:
        ans = ans1
        break
    elif sum - ans1 > target:
        end = mid - 1
    else:
        start = mid+1




print(ans)

