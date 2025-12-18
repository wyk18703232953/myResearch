ints=[int(x) for x in input().split()]
n=ints[0] # number of ints
m=ints[1] # num special
k=ints[2] # divider
special=[int(x) for x in input().split()]
numOn=0
numOps=0
while numOn<m:
    numOps+=1
    op=((special[numOn]-numOn-1)//(k))*k+k+numOn+1
    while numOn<m and special[numOn]<op:
        numOn+=1
print(numOps)