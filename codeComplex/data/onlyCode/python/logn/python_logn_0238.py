n, s = map(int, input().split())
mult_10 = s if not (s%10) else s+10-(s%10)
for i in range(mult_10, mult_10+100000, 10):
	if i - sum([int(c) for c in str(i)]) >= s:
		low = i
		break
print(max(n-low+1, 0))
		   		 	 	  	  	 			     				