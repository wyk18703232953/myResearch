n = int(input())

dt = input()
s = dt.split()
a = [int(x) for x in s]
sortm = [int(x) for x in s]

sortm.sort()

cnt = 0

for i in range(n):
	if a[i] != sortm[i]:
		cnt += 1


if cnt <= 2:
	print("YES")
else:
	print("NO")
	 	  		 	  	 	  			    	  	 	 	