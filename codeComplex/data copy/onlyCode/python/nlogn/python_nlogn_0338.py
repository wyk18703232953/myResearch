n = int(input())
ar = []
for i in range(n):
    ar.append(input())
sortedAr = sorted(ar,key=len)
flag = False
for i in range(n-1):
    if sortedAr[i+1].find(sortedAr[i]) == -1:
        print('NO')
        flag = True
        break
if not flag:
    print('YES')
    for i in sortedAr:
        print(i)
 	 	 	    			 	   	 	 			 	 		