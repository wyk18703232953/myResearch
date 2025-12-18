n,m,k = map(int,input().split())
pi = list(map(int,input().split()))
num = 1
ans = 0
i = 0
while i < m:
    temp = (pi[i] - num) // k
    temp2 = i
    i += 1
    while i < m :
        if temp != (pi[i] - num) // k:
            break
        i += 1
    num += (i - temp2)
    ans += 1
print(ans)
