n, t = map(int, input().split())
 
a, v = sorted(list(map(int, input().split())) for i in range(n)), 2
 
for i in range(n - 1):
 
    d = 2 * a[i + 1][0] - a[i + 1][1] - 2 * a[i][0] - a[i][1]
 
    if d > 2 * t:
 
        v += 2
 
    elif d == 2 * t:
 
        v += 1
 
print(v)