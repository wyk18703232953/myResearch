def Sort(x):
	if len(x) == 1:
		return x
		
	a = Sort(x[:len(x) // 2])
	b = Sort(x[len(x) // 2:])
	
	c = []
	i = 0
	j = 0
	while (i < len(a))and(j < len(b)):
		if a[i] < b[j]:
			c.append(a[i])
			i += 1
		else:
			c.append(b[j])
			j += 1
	
	c = c + b[j:]
	c = c + a[i:]
	
	return c

input()
m = [int(i) for i in input().split(' ')]

newm = Sort(m)
count = 0
for i in range(len(m)):
 if newm[i] != m[i]:
  count += 1

if count / 2 <= 1:
 print('YES')
else:
 print('NO')
    	   				  	  	 		  				   	