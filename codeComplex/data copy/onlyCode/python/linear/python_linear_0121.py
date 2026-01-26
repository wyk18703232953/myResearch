n= int(input())
t=[[] for _ in range(n+1)]
for i in range(n-1):
    v = int(input())
    t[v].append(i+2)
#print(t)
flag=True
for l in t:
    if l!=[]:
        cnt=0
        for ele in l:
            if t[ele]==[]:
                cnt+=1
        if cnt<3:
            flag=False
            break
if flag:
    print("YES")
else:
    print("NO")