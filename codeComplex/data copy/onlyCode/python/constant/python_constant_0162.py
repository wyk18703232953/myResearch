k = 1000001
a = [True] * k
a[0] = a[1] = False

for i in range(k):
    if a[i]:
        for j in range(2*i, k, i):
            a[j] = False

n = int(input())
for i in range(4, n):
    if not a[i] and not a[n-i]:
        print(i, n-i)
        exit()