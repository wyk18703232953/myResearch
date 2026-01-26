reduced = 1
n, m ,k = map(int,input().split())

p = list(map(int, input().split()))

p.reverse()
cnt = 0
while(len(p)):
    
    cnt1 = 1
    first = p.pop()
    fack = ((first - reduced)//k) * k
    while(len(p) and p[-1] - fack - reduced < k):
        cnt1 += 1
        p.pop()
    
    reduced += cnt1
    cnt += 1
print(cnt)