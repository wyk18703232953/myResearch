m, n = map(int, input().split())
a = [int(input()) for q in range(m)]
a.append(10**9)
s = []
for q in range(n):
    f, g, d = map(int, input().split())
    if f == 1:
        s.append(g)
a.sort()
s.sort()
q1 = 0
min1 = float('inf')
for q2 in range(len(a)):
    while q1 < len(s) and a[q2] > s[q1]:
        q1 += 1
    if min1 > q2+len(s)-q1:
        min1 = q2+len(s)-q1
    if q1 == len(s):
        break
print(min1)
