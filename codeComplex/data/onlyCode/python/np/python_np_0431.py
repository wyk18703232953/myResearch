def get_ans(x, a, n, m):

    lim = 1<<m
    match = lim-1
    track = [-1 for i in range(lim)]

    for i in range(n):
        mask = 0
        for j in range(m):
            if(a[i][j] >= x):
                mask |= 1 << j
        track[mask] = i

    for i in range(lim):
        for j in range(lim):
            if(i|j == match and track[i] != -1 and track[j] != -1):
                return track[i], track[j]
    
    return -1, -1


n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

lo = 0
hi = 1000000000
while(lo < hi-1):
    mid = (lo+hi)/2
    i, j = get_ans(mid,a,n,m)
    if(i == -1):
        hi = mid-1
    else:
        lo = mid

i,j = get_ans(hi,a,n,m)
if(i != -1):
    print("{} {}".format(i+1,j+1))
else:
    i,j = get_ans(lo,a,n,m)
    print("{} {}".format(i+1,j+1))
