n,k = map(int, input().split()) 

v = list(map(int, input().split()))
v.sort()
ans = 0
cnt = 0
ar = [0]  * 1000000
for i in range(len(v)):
    while  cnt>0 and v[i] > ar[cnt] and v[i] <= k+ar[cnt] :
        cnt=cnt-1
    cnt = cnt + 1
    ar[cnt] = v[i]
print(cnt)