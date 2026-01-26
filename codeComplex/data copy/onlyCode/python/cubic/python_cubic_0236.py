R, G, B = list(map(lambda x: int(x), input().split()))
r = list(map(lambda x: int(x), input().split()))
g = list(map(lambda x: int(x), input().split()))
b = list(map(lambda x: int(x), input().split()))

def f(t):
    i, j, k = t
    return (i+1)*(G+1)*(B+1) + (j+1)*(B+1) + (k+1)

max_area = [None]*((R+1)*(G+1)*(B+1)+1)

def get_max_area(i, j, k):
    temp = f((i,j,k))
    if max_area[temp] != None:
        return max_area[temp]
    x1=x2=x3=0
    if i >= 0 and j>=0:
        x1 = get_max_area(i-1, j-1, k) + r[i]*g[j]
    if i >= 0 and k >= 0:
        x2 = get_max_area(i-1, j, k-1) + r[i]*b[k]
    if j >= 0 and k >= 0:
        x3 = get_max_area(i, j-1, k-1) + g[j]*b[k]

    max_area[temp] = max(x1, x2, x3)
    return max_area[temp]

r.sort()
g.sort()
b.sort()
print(get_max_area(R-1, G-1, B-1))
#print(max_area)    