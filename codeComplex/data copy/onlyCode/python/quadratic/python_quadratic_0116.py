n,m=map(int,input().split())
c=input().split()
col=[0]*n
for i in range(len(c)):
    col[int(c[i])-1]+=1
print(min(col))