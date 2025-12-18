n,k = map(int,input().split())

def sumTillN (n) :
    return (n*(n+1))//2

minEat = 0
maxEat = n
midEat = 0

while (minEat<=maxEat):
    midEat = (minEat+maxEat)//2
    x = sumTillN(n-midEat)
    if (x==k+midEat):
        break
    elif (x>k+midEat):
        minEat = midEat+1
    else:
        maxEat = midEat-1

print(midEat)
