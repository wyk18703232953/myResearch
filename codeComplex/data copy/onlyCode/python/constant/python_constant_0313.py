A = list(map(int, input().split()))

ans = 0
for i in range(14):
    if A[i] == 0:
        continue
    B = A+A
    B[i+14] = 0
    q, r = divmod(B[i], 14)
    for j in range(1, 15):
        if j <= r:
            B[i+j] += (q+1)
        else:
            B[i+j] += q
    #print(A[i], B)
    temp = 0
    for j in range(i+1, i+15):
        if B[j]%2 == 0:
            temp += B[j]
    ans = max(ans, temp)
print(ans)
