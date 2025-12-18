import sys
input = sys.stdin.readline

a,b,c = list(map(int,input().split()))

x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = list(map(int,input().split()))

x.sort(reverse=True)
y.sort(reverse=True)
z.sort(reverse=True)

a+=1
b+=1
c+=1

x = [0] + x
y = [0] + y
z = [0] + z

tmp = [[0]*c for _ in range(b)]
best = [tmp for _ in range(a)]

#print(tmp)
#print(best)
ans = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            if (i+j+k) % 2 == 0:
                aa,bb,cc = 0,0,0
                if i>0 and j>0:
                    aa = best[i-1][j-1][k] + x[i] * y[j]
                if i>0 and k>0:
                    bb = best[i-1][j][k-1] + x[i] * z[k]
                if j>0 and k>0:
                    cc = best[i][j-1][k-1] + y[j] * z[k]
                
                best[i][j][k] = max(aa,bb,cc)
                ans = max(ans, best[i][j][k])
#print(best)
print(ans)
