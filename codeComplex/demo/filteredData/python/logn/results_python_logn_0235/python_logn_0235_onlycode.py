n,s=map(int,input().split())
if s>=n:
    print("0")
    exit()
for i in range(s,n+2):
    cur=int(0)
    for j in str(i):
        cur+=int(j)
    if i-cur>=s:
        break
print(n-i+1)
