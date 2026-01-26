import sys 
n=int(input())
ind=0
dig=0
for i in range(1,12):
    dig+=i*10**(i-1)*9 
    #print(dig)
    if dig>n:
        ind=i-1
        rt=dig-i*10**(i-1)*9 
        break 
n-=rt
no=10**ind
#print(n)
if n==0:
    print(9)
    sys.exit()
u=n
n-=(n//(ind+1))*(ind+1)
no+=max(0,(u//(ind+1))-1)
#print(n)
if n==0:
    print(str(no)[-1])
else:
    no+=1
while(n>0):
    if n<=ind+1:
        e=str(no)
        print(e[n-1])
    n-=ind+1
    no+=1

