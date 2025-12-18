l,r = map(int,input().split())
ans = l ^ r
x = bin(ans)[1:]
if ans == 0:
    print(0)
else:
    ptr = -1
    po = 0
    while True:
        if( x[ptr] == '0') :
            ans += 2**po
        po += 1
        ptr-=1
        if( ptr == -len(x)-1 ):
            break

    print(ans)
