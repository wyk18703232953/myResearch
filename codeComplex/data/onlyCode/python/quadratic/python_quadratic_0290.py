n = int(input())
a = list(map(int, input().split()))
ans = 0
pos = 2*n - 2
for i in range(n):
	x = a[-1]
	a.pop(-1)
	y = a.index(x)
	ans += pos - y
	pos -= 2
	a.pop(y)
print(ans)
 	 	   			   		  		  	       	