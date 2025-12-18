n,r = map(int,input().split())
x_coord = list(map(int,input().split()))
d = {}
for i in x_coord:
    final = r
    for j in range(i-r,i+r+1):
        check = d.get(j,[-1,-1])
        if check[0] > 0:
            potential = check[1] + ((4*r*r)-((i-check[0])**2))**.5
            final = max(potential,final)
    for j in range(i-r,i+r+1):
        d[j] = (i,final)
    print(final,end = " ")