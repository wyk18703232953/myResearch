def possible(arr):
    # 4 possible cases

    a,b,c,d,e,f = arr
    if(a == c == e and b + d + f == a):
        one = "A" * b + "B" * d + "C" * f
        print(a)
        for i in range(a):
            print(one)
        return True
    if(b == d == f and a + c + e == d):
        print(b)
        for i in range(a):
            print("A" * b)
        for i in range(c):
            print("B" * b)
        for i in range(e):
            print("C" * b) 
        return True
    ns = [(a,b,"A"),(c,d,"B"),(e,f,"C")]
    fs = [(b, a,"A"),(d, c,"B"),(f, e,"C")]
    ns.sort(reverse = True)
    x,y,z = ns
    a,b,t1 = x
    c,d,t2 = y
    e,f,t3 = z
    if(c + e == a and d == f and d + b == a):
        print(a)
        mat = [["." for i in range(a)] for j in range(a)]
        for i in range(a):
            for j in range(b):
                mat[i][j] = t1
        for i in range(c):
            for j in range(b, a):
                mat[i][j] = t2
        for  i in range(c, a):
            for j in range(b, a):
                mat[i][j] = t3
        for i in range(a):
            print("".join(mat[i]))
        return True

    fs.sort(reverse = True)
    x,y,z = fs
    b,a,t1 = x
    d,c,t2 = y
    f,e,t3 = z
    if(d + f == b and c == e and c + a == b):
        print(b)
        mat = [["." for i in range(b)] for j in range(b)]
        for i in range(a):
            for j in range(b):
                mat[i][j] =t1
        for i in range(a, b):
            for j in range(d):
                mat[i][j] = t2
        for i in range(a, b):
            for j in range(d, b):
                mat[i][j] = t3
        for i in range(b):
            print("".join(mat[i]))
        return True
    return False

arr = [int(x) for x in input().split()]
cnt = 0
ok = False
for i in range(8):
    send = [x for x in arr]
    if(i&1):
        send[0], send[1] = send[1], send[0]
    if(i&2):
        send[2], send[3] = send[3], send[2]
    if(i&4):
        send[4], send[5] = send[5], send[4]
    if(possible(send)):
        ok = True
        break
if(not ok):
    print(-1)

