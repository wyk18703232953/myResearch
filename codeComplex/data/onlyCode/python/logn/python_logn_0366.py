mod = 1000000000+7
def fp(x ,y):
    if y == 1:
        return x
    if y == 0:
        return 1
    t = fp(x,y//2)%mod
    if y%2 == 1:
        return (t*t*x)
    else:
        return (t*t)

def inv(x):
    return fp(x%mod,mod-2)%mod

n,k=list(map(int,input().split()))
if not n:
    print(0)
    exit()
if not k:
    print( (2*n)%mod )
    exit()
numberOfPro =fp(2,k)
last = n*numberOfPro
first = (n-1)*numberOfPro+1
sumOfLast = (last)*(last+1)*inv(2)
sumOfFirst = first*(first-1)*inv(2)
num = 2*(sumOfLast - sumOfFirst)*inv(numberOfPro)
print(num%mod)
