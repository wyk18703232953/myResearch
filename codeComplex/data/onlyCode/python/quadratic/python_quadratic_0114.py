def ints():
 return map(int,input().split())
n,m=ints()
c=ints()
aa=[0]*(n+1)
for cc in c:
 aa[cc]+=1
print(min(aa[1:]))
 			  			 		 		 		  		 		  	