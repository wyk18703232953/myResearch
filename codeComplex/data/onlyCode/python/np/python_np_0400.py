def isPoss(n, arrs, nvals):
    masks = set()
    midx = {}
    for pos,arr in enumerate(arrs):
        mask = 0
        for i in range(nvals):
            if arr[i]>=n:
                mask += 1<<i
        midx[mask] = pos+1
        masks.add(mask)

    for m1 in masks:
        for m2 in masks:
            if m1|m2 == (1<<nvals)-1:
                return midx[m1], midx[m2]

    return -1, -1
                

narr, nvals = map(int, input().split())

arrs = []
for i in range(narr):
    arrs.append(list(map(int, input().split())))

mn = -1
mx = 10**9+1
while mn < mx-1:
    mid = (mn + mx) // 2
    a,b = isPoss(mid, arrs, nvals)
    if a != -1:
        mn = mid
    else:
        mx = mid - 1

for i in range(1,-1,-1):      
    a,b = isPoss(mn+i, arrs, nvals)
    if a != -1:
        print(a,b)
        break

