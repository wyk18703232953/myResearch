n, k = map(int, input().split())
a = list(map(int, input().split()))
j = 0
a.sort()
n1 = n
for i in range(n):
    while a[j] < a[i]:
        if a[i] <= a[j] + k:
            n1 -= 1
        j += 1
print(n1)
