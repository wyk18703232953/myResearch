n, k = [int(i) for i in input().split()]
a, j = sorted([int(i) for i in input().split()]), 0
for i in a:
    while i > a[j]:
        if i <= a[j] + k:
            n -= 1
        j += 1
print(n)