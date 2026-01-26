n, k = [int(i) for i in input().split()]

mid = n//2
leftside = 1
rightside = n

candies = n-mid

while mid * (mid + 1)//2 - candies != k:
    if k > mid * (mid + 1)//2 - candies:
        leftside = mid + 1
    else:
        rightside = mid

    mid = (leftside + rightside)//2
    candies = n-mid
print(candies)