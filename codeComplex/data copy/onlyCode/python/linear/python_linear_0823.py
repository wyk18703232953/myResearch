from math import*
n,k=map(int,input().split())
s=1
dob=2
for i in range(1,n):
    s+=dob
    dob+=1
    if s-(n-i-1)==k:
        print(n-i-1)
        exit()
print(0)

