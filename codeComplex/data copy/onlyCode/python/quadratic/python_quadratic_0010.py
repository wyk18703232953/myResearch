# Collaborated with Rudransh Singh

from math import sqrt
n, r = input().split()
n = int(n)
r = int(r)
x = []
arr = []
inpArr = input().split(" ")
for i in inpArr:
    x.append(int(i))
    
for i in range(n):
    arr.append(r)
    for j in range(i):
        if (abs(x[j] - x[i]) <= (r * 2)):
            arr[i] = max(arr[i], (arr[j] + sqrt((r*r*4)-((x[j] - x[i])*(x[j] - x[i])))  ))
arr1 = []
for i in arr:
    arr1.append(str(i))
print(" ".join(arr1))
		 	  	 		 	 		   		 	 	    	 	