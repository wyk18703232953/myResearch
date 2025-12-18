n=int(input())
ls=list(map(int,input().split()))
ls.sort()
if ls.count(min(ls))==len(ls):
	print('NO')
for i in range(n):
	if ls[i]!=min(ls):
		print(ls[i])
		break
	   	 		    			 	  	  		 			  	