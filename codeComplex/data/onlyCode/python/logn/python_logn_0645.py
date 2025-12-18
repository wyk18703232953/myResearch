left = -1
right = 10e9 - 1
nn = [int(i) for i in input().split()]
n = nn[0]
k = nn[1]
f = True
while right - left > 1:
    mid = (left + right) // 2
    if ((n - mid + 1) * abs((n - mid)) // 2 - mid > k):
        left = mid
    else:
        if((n - mid + 1) * abs((n - mid)) // 2 - mid == k):
            print(round(mid))
            f = False
            break
        else:
            right = mid
if f:
    print(round(left))
            
                