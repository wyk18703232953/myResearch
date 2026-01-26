n , s = map(int,input().split())
a = [0] * (n+1)
for _ in range(n-1) :
    u , v=map(int, input().split())
    a[u] += 1
    a[v] += 1
print(2.0*s/a.count(1))