n=int(input())
a=input()
b=a.count('T')
c=-1
for i in range(n):
    d=0
    for j in range(b):
        d+=int(a[(i+j)%n]=='H')
    if c==-1 or d<c:
        c=d
print(c)