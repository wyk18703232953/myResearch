def out_edge(x,y):
    a[x] -= 1
    a[y] -= 1
    print(x,y)


n = int(input())
a =list(map(int, input().split()))
sa = sum(a)
ma = min(a)
if (sa <2*(n-1)) or (ma<1):
    print('NO')
    exit()

verts = sorted(enumerate(a,1), key = lambda x: x[1], reverse= True)
verts = [list(j) for j in verts]
outres = []
for kk in range(1,n):
    if  verts[kk-1][1] >= 1:
        outres.append((verts[kk] [0], verts[kk-1][0]))
        verts[kk][1] -= 1
        verts[kk-1][1] -= 1
    else:
        break
else:
    kk+=1

path_len = kk
# print(kk)
print('YES', min(n-1, path_len))

reserve_start = 0
while kk < n:
    if verts[reserve_start][1] >0:
        outres.append((verts[reserve_start][0], verts[kk][0]))
        verts[reserve_start][1] -= 1
        verts[kk][1] -= 1
        kk +=1
    else:
        reserve_start += 1

print(len(outres))
for oo in outres:
    print(*oo)







