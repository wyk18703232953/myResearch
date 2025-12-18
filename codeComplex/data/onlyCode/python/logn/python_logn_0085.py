l, r = map(int, input().split())

if l == r:
    print(0)
    exit()

x = 1
while x <= r:
    x = x << 1
x = x >> 1

k = x
while x <= l or x > r:
    if x <= l:
        x += k
    else:
        x -= k
    k = k >> 1

print(x ^ (x - 1))
   				 			    	     				   			