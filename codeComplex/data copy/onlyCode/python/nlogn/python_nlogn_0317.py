n=int(input())
w=[int(k) for k in input().split()]
c={w[j]:j+1 for j in range(n)}
#print(c)
res=0
for j in range(1, n+1):
    if w[j-1]==j:
        pass
    else:
        res+=1
        y=w[j-1]
        w[j-1]=j
        w[c[j]-1]=y
        r=c[j]
        c[j]=j
        c[y]=r
if n%2==0:
    if res%2==0:
        print("Petr")
    else:
        print("Um_nik")
else:
    if res%2:
        print("Petr")
    else:
        print("Um_nik")
#print(w)