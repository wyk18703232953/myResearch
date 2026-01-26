a , b , c , d , e , f = map(int,input().split())
n , n1 = 1 , a * b + c * d + e * f
while n ** 2 < n1 :
    n += 1
if n ** 2 > n1 :
    print(-1)
    exit()
l = sorted([[max(a,b),min(a,b),'A'], [max(c,d),min(c,d),'B'], [max(e,f),min(e,f),'C']])
if l[2][0] != n:
    print(-1)
    exit()
v = str(n) + '\n' + (l[2][2] * n + '\n') * l[2][1]
if l[0][0] == n and l[1][0] == n:
    for i in range(2):
        v += (l[i][2] * n + '\n') * l[i][1]
else:
    s = n - l[2][1]
    if s not in l[0] or s not in l[1] :
        print(-1)
        exit()
    x , y = l[0][1] if s == l[0][0] else l[0][0] , l[1][1] if s == l[1][0] else l[1][0]
    v += (l[0][2] * x + l[1][2] * y + '\n') * s
print(v)