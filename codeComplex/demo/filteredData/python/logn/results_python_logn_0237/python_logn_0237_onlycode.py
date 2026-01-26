n, s = map(int, input().split())
x, y = divmod(s, 9)
if not s:
	x = 0
elif y:
	x += 1
low = x*9
for i in range(low, low+10000):
	if i - sum([int(c) for c in str(i)]) >= s:
		low = i
		break
print(max(n-low+1, 0))
				  	 			 		  				 			   	