s=input()
a=list(map(int,input().split()))
k=sorted(a)
b=0
q=0
m=0
for i in k:
    b=b+i
for i in k[::-1]:
    q=q+i
    m=m+1
    if q>(b/2):
        break
print(m)    