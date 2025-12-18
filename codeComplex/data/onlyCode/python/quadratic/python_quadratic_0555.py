n, m=[int(k) for k in input().split()]
res=[]
for j in range(n//2):
    for k in range(m):
        res.append(str(j+1)+" "+str(k+1))
        res.append(str(n-j)+" "+str(m-k))
if n%2:
    for j in range(m//2):
        res.append(f"{n//2+1} {j+1}")
        res.append(f"{n//2+1} {m-j}")
    if m%2:
        res.append(f"{n//2+1} {m//2+1}")
print("\n".join(res))