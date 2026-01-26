n = int(input())
flag = True
l , r = list(map(int,input().split())) , list(map(int,input().split()))
ans , check_l , check_r = [n for i in range(n)] , [0 for i in range(n)] , [0 for i in range(n)]
for i in range(n):
    ans[i] -= l[i]+r[i]
for i in range(n):
    cl , cr = 0 , 0
    for j in range(i):
        if ans[j] > ans[i]:
            cl += 1
    for j in range(i+1,n):
        if ans[j] > ans[i]:
            # print(l[j],l[i],j,i)
            cr += 1
    # print(cl,cr)
    if cl != l[i] or cr!=r[i]:
        flag = False
        break
mini = min(ans) - 1
for i in range(n):
    ans[i] -= mini
# print(ans,check_l,check_r,sep='\n')
if flag:
    print("YES")
    for i in ans:
        print(i,end= ' ')
else:
    print("NO")