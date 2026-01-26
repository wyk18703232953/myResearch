n,U=map(int,input().split())
Ar=list(map(int,input().split()))
R = 0;
ans = -1;
for i in range(n):
    while R + 1 < n and Ar[R + 1] - Ar[i] <= U:
        R+=1
    if i+1 < R:
        ans = max((Ar[R] - Ar[i + 1]) / (Ar[R] - Ar[i]),ans);
print(ans)
