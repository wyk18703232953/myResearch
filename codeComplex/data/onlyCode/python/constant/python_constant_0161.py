k = 1000001
a = [True] * k
a[0] = a[1] = False

for i in range(k):
    if a[i]:
        j = 2 * i
        while j < k:
            a[j] = False
            j += i

n = int(input())
for i in range(4, n):
    if not a[i] and not a[n-i]:
        print(i, n-i)
        exit()