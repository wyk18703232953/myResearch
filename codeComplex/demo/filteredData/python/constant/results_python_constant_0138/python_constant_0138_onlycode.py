a, b = map(int, input().split(' '))
res = 0
temp = 0

if a%b == 0:
    print(int(a/b))
else:
    while b!=0:
        res += a//b
        a%=b
        temp = a
        a = b
        b = temp
    print(res)
			     			  				 				 			  		