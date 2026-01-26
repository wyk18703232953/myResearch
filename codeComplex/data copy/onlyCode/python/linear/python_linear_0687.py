n = int(input())
b = [int(w) for w in input().split()]
a = [0]*n

l = n//2 - 1
r = n//2

a[l] = b[l] // 2
a[r] = b[l] - a[l]

while l > 0:
    if b[l-1] >= b[l]:
        a[l-1] = a[l]
        a[r+1] = b[l-1] - a[l]
    else:
        a[r+1] = a[r]
        a[l-1] = b[l-1] - a[r]
    l -= 1
    r += 1

print(*a)
