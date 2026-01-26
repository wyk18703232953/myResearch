n=int(input())
w=[int(k) for k in input().split()]
m=int(input())
c=0
for i in range(n):
    for j in range(i+1, n):
        if w[i]>w[j]:
            c+=1
c%=2
for j in range(m):
    l, r=[int(k) for k in input().split()]
    x=r-l+1
    if x!=1 and (x*(x-1)//2)%2:
        c=not c
    if c:
        print("odd")
    else:
        print("even")