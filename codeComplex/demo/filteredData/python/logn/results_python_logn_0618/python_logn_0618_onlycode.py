ints=[int(x) for x in input().split()]
# (numEat+numTimePut)=n
# (numTimePut*(numTimePut+1))//2-numEat=k
# ((numTimePut*(numTimePut+1))//2)-k+numTimePut=n
# ((numTimePut*(numTimePut+3))//2)=n+k
# (2*numTimePut)*(2*numTimePut+6)=8(n+k)
# (2*numTimePut)*(2*numTimePut+6)+9=8(n+k)+9
# (2*numTimePut+3)**2=8(n+k)+9
# numEat=n-((8(n+k)+9)**(1/2)-3)/2
n=ints[0]
k=ints[1]
print(int(n-((8*(n+k)+9)**(1/2)-3)/2))