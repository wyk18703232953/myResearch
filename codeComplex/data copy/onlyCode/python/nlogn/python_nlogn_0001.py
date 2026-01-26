def good(x1, y1, x2, y2):
    if (x1 > x2):
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    return (x2 >= y1) 

def check(cent):
    for i in range(n):
        if (not good(cent - t, cent + t, x[i] - a[i], x[i] + a[i])):
            return 0
    return 1

n, t = map(int, input().split())
x = [0] * n
a = [0] * n
for i in range(n):
    x[i], a[i] = map(int, input().split())
    x[i] *= 2

ans = set()

for i in range(n):
    val1 = x[i] - a[i] - t
    val2 = x[i] + a[i] + t
    if (check(val1)):
        ans.add(val1)
    if (check(val2)):
        ans.add(val2)
print(len(ans))
