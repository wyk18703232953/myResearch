import math

v = [int(x) for x in input().split()]
n = len(v)
val = 0
for i in range(n):
    a = v[i] // n
    arr = v.copy()
    arr[i] = 0
    for j in range(n):
        arr[j] += a
    b = v[i] % n
    k = i + 1
    l = 0
    while l < b:
        if k > n - 1:
            k = 0
        arr[k] += 1
        k += 1
        l += 1

    count = 0
    for j in range(n):
        if arr[j] % 2 == 0:
            count += arr[j]
    val = max(val, count)
print(val)





