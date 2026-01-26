import math as m

nDiscs, r = [int(x) for x in input().split()]

x = [int(x) for x in input().split()]
y = []

for i in range(len(x)):
    tempY = [r]
    for j in range(i):
        diffX = abs(x[i] - x[j])
        if diffX <= (2 * r):
            addY = m.sqrt((4 * r * r) - (diffX * diffX))
            tempY.append(y[j] + addY)
    y.append(max(tempY))

for i in range(len(y)):
    print(y[i], end=' ')
print()

		 	   				    	 	 		  	 			  	