k = int(input())
x = [0,9]
i = 2
y = 90
while x[-1] < 10**12:
    x.append(x[-1]+y*i)
    y *= 10
    i += 1
if k in x:
    print(9)
else:
    for t in range(len(x)):
        if k < x[t]:
            break
    e = k-x[t-1]
    if t == 1:q=str(e)
    else:q =str(10**(t-1)+e//t-1)
    if e%t == 0:
        print(q[-1])
    else:
        q = str(int(q)+1)
        print(q[e%t-1])
