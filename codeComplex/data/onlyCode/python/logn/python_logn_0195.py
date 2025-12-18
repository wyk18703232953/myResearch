n, s = map(int, input().split())

def binsearch(n, s):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        digits = sum([int(i) for i in list(str(mid))])
        if mid - digits >= s:
            right = mid - 1
        else:
            left = mid + 1

    return right
#print(binsearch(n, s))
print(max(0, n - binsearch(n, s)))

