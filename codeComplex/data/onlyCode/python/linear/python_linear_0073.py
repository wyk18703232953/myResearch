a , b = input(), input()
ans = 0
 
ones = [0 for i in range(len(b)+1)]
zeros = [0 for i in range(len(b)+1)]
 
for i in range(len(b)):
    ones[i] = ones[i-1] + int(b[i])
    zeros[i] = i + 1 - ones[i]
    
for i in range(len(a)):
    if a[i] == '1':
        ans += zeros[len(b)-len(a)+i] - zeros[i-1]
 
    else:
        ans += ones[len(b)-len(a)+i] - ones[i-1]
 
print(ans)
  	 	   	     	 				 	     			