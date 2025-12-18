n=int(input())
s=0
i=1
c=1
while(s<n):
    s+=9*i*c
    c+=1
    i*=10
n=n-s+9*i*(c-1)//10
c=c-1
r=n%c
d=n//c
k=10**(c-1)+d
if(r==0):
    print(int(str(k-1)[-1]))
else:
    print(int(str(k)[r-1]))

