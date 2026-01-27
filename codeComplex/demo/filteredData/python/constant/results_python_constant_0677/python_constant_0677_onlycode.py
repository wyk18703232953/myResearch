from sys import stdout
m = 30
a, b = 0, 0
fle = 1
for i in range(m):
    if fle:
        print('? {} {}'.format(a, b))
        stdout.flush()
        resp1 = int(raw_input())
        fle = 0
    print('? {} {}'.format(a + 2**(m-1-i),b + 2**(m-1-i)))
    stdout.flush()
    resp2 = int(raw_input())
    #print(resp1,resp2,a,b)
    if resp1 == -1 and resp2 == 1:
        b += 2**(m-1-i)
        fle = 1
    elif resp1 == 1 and resp2 == -1:
        a += 2**(m-1-i)
        fle = 1
    else:
        fle = 0
        print('? {} {}'.format(a + 2**(m-1-i), b))
        stdout.flush()
        resp3 = int(raw_input())
        if resp3 == -1:
            b += 2**(m-1-i)
            a += 2**(m-1-i)
        #print(resp1,resp2,resp3,a,b)
print('! {} {}'.format(a,b))
stdout.flush()