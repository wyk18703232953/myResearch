t = int(input())

for i in range(0, t) :
    n, k = [int(x) for x in input().split()]
    if (n >= 32) :
        print("YES %d" % (n-1))
    else :
        low=0
        co=-1
        md = [0]
        for j in range(1, n):
            md.append(md[-1]*4 + 1)
        kk = 0
        found=0
        for cut in range(1,n+1) :
            low += (1<<cut)-1
            co = 2*co + 3
            kk += co*md[n-cut]
            if (k>=low and k<=low+kk) :
                print("YES %d" % (n-cut))
                found=1
                break
        if (found == 0) : print("NO")
