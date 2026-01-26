import sys
def getSum(a):
    sum1 = a * (a + 1) // 2
    return sum1
def getSumOfTwo(a, b):
    if a <= 1:
        return getSum(b)
    return getSum(b) - getSum(a - 1)

n, k = [int(elem) for elem in input().split()]
if n == 1:
    print(0)
    sys.exit(0)
if n <= k:
    print(1)
    sys.exit(0)
if getSum(k - 1) < n - 1:
    print(-1)
    sys.exit(0)

n -= 1
k -= 1
left, right = 1, k
while left < right:
    mid = (left + right) // 2
    sum1 = getSumOfTwo(mid, k)
    if sum1 == n:
        print(k - mid + 1)
        sys.exit(0)
    if sum1 > n :
        left = mid + 1
    else:
        right = mid
print(k - left + 2)
		 			  			  			 	  				    		