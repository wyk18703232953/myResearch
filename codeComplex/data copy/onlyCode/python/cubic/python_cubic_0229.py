R,G,B = list(map(int, input().split()))
r = sorted(list(map(int, input().split())), reverse =True)
g = sorted(list(map(int, input().split())), reverse =True)
b = sorted(list(map(int, input().split())), reverse =True)
def f(x,y,z):
    m1 = 0
    m2 = 0
    m3 = 0
    if(x<R and y<G):
        if(dpt[x+1][y+1][z]==-1):
            dpt[x+1][y+1][z] = f(x+1,y+1,z)
        m1 = r[x]*g[y] + dpt[x+1][y+1][z]
    if(y<G and z<B):
        if(dpt[x][y+1][z+1]==-1):
            dpt[x][y+1][z+1] = f(x,y+1,z+1)
        m2 = g[y]*b[z] + dpt[x][y+1][z+1]
    if(z<B and x<R):
        if(dpt[x+1][y][z+1]==-1):
            dpt[x+1][y][z+1] = f(x+1,y,z+1)
        m3 = r[x]*b[z] + dpt[x+1][y][z+1]
    dpt[x][y][z] = max(m1,m2,m3)
    return dpt[x][y][z]
dpt = [[[-1 for _ in range(B+1)]for _ in range(G+1)]for _ in range(R+1)]
print(f(0,0,0))