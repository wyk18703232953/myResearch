n=int(input())
i=iter(sorted(zip(map(int,input().split()),range(1,n+1))))
s,o=[],[]
for c in input():
 if c=='0':
  x=next(i)[1];o+=[x];s+=[x]
 else:o.append(s.pop())
print(*o)
	  	 		    				 	 	 				 	   	