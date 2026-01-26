n=int(input())
a=list(map(int,input().split()))
leaf=[i+1 for i in range(n) if a[i]==1]
root_w=[i+1 for i in range(n) if a[i]!=1]
root_r=[a[i-1]-2 for i in root_w]
l_path=root_w
if(len(leaf)!=0):
    l_path=[leaf[0]]+l_path
    leaf=leaf[1:]
if(len(leaf)!=0):
    l_path=l_path+[leaf[0]]
    leaf=leaf[1:]

if sum(root_r)<len(leaf):
    print("NO")
else:
    print("YES {}".format(len(l_path)-1))
    print(n-1)
    for i in range(len(l_path)-1):
        print("{} {}".format(l_path[i],l_path[i+1]))
    for l in leaf:
        while(len(root_r)>0 and root_r[0]==0):
            root_w = root_w[1:]
            root_r = root_r[1:]
        print("{} {}".format(l,root_w[0]))
        root_r[0] = root_r[0]-1
