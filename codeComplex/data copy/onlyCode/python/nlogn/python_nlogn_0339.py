n=int(input())
l=[input() for i in range(n)]
#print(l)
s=sorted(l,key=len)
for i in range(1,n):
    if s[i-1] not in s[i]:
        print("NO")
        exit()
# else:
print("YES")
for i in s:
    print(i)
	     	 		  	   		   		 			 		