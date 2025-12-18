n, k  = map(int, input().split())
a = []
b = []
c = 0
d = []


for i in range(n):
    x, y= map(int, input().split())
    t = x-y
    a.append(x)
    b.append(y)
    d.append(t)
s = sum(a)
d.sort()
d = d[::-1]
if sum(b)>k:
    print(-1)
else:
    while s>k:                #we are seeing how many cases we have to consider
                                # and in each considered case we wil remove the extra part
                                #we sort in descnending order to get as much profit as possible
                                #and we subtract irrespective of which elemenet we remove.
        s = s - d[c]
        c = c + 1
    print(c)



