n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
s1 = 0
s2 = sum(a)

for i in range(len(a)):
    s1 += a[i]
    s2 -= a[i]
    if s1 > s2:
        break

print(i + 1)