def bin(a):
    if a <= 1:
        return a
    else:
        return 10*bin(a//2)+a%2

def convBin(a):
    k,i = 0,0
    while a!=0:
        k += (a%10)*int((2**i))
        a //= 10
        i += 1
    return k

def maxi(a,b):
    if a == b:
        return 0
    elif a+1 == b:
        return a^b
    elif a+2 == b:
        x = a^(a+1)
        y = a^(a+2)
        z = (a+1)^(a+2)
        return max(max(x,y),z)
    else:
        x = str(bin(a^b))
        y = '1'*len(x)
        return convBin(int(y))
a = list(map(int,input().split()))
print(maxi(a[0],a[1]))
