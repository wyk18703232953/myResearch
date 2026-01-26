def number(pos):
    ans = 0
    for i in range(pos + 1):
        ans += 2**(i)
    return ans

l, r = input().split()
l = int(l)
r = int(r)

if(l == r):
    print(0)
else:
    b_pos = 0
    i = 0
    while(l > 0 or r > 0):
        if(l%2 != r%2):
            b_pos = i
        l >>= 1
        r >>= 1
        i += 1
    print(number(b_pos))

	 		 	 	 	 	  	  				  	 	 	