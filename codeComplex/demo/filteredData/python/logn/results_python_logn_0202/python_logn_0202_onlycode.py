n,s = input().split()

i = int(s)
d_sum = sum(list(map(int,str(i))))
while i - d_sum < int(s):
    i += 1
    d_sum = sum(list(map(int,str(i))))  

print((max(0,int(n)-i+1)))
			   	   	 					 		      		