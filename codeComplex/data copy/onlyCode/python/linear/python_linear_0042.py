n, k= map(int, input().split())
A = list(map(int, input().split()))
C = [0] * 100001

l = 0
r = 0
p = 0

while r<n and p < k:
    C[A[r]] += 1
    if C[A[r]] == 1:
        p += 1
    r += 1
if p != k:
    print('-1', '-1')
else:
    while p == k:
        C[A[l]] -= 1
        if C[A[l]] == 0:
            p -= 1
        l +=1
        
    l -= 1
    
    print(l+1,r)