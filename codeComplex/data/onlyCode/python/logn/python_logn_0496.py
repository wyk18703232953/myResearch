n=input()
i=0
while(True):
    if (n-9*10**i*(i+1))<=0:
        break
    n-=9*10**i*(i+1)
    i+=1

a=n/(i+1)
b=n%(i+1)
if(b!=0):
    print(str(10**i+a)[b-1])
else:
    print(str(10**i+a-1)[-1])
