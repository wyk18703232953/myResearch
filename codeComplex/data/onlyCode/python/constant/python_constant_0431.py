n, k = (int(x) for x in input().split())
 
if k > n * 2 or k < 3:
    print(0)
elif n >= k-1:
    print(k - k//2 - 1)
else:
    print(n - k//2)