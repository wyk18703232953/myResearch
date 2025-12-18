left, right = [int(x) for x in input().split(' ')]

if left == right:
    print(0)
else:
    x = 1
    while x <= right:
        x *= 2
    x //= 2
    y = x
    while y > 0 and x <= left or x > right:
        if x <= left:
            x += y
        else:
            x -= y
        y //= 2
    print(x^(x-1))
	  		   		  			  						 			 	