import sys
def input():    return sys.stdin.readline().strip()
def iinput():   return int(input())
def rinput():   return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))

n=iinput()
d={}
for i in range(n - 1):
    u,v=rinput()
    d.setdefault(u,[]).append(v)
    d.setdefault(v,[]).append(u)
node=1
for key in d:
    if(len(d[key])>len(d[node])):
        node=key
ans=[]
visited=[0]*n
visited[node-1]=1
for c in d[node]:
    while(True):
        visited[c-1]=1
        if(len(d[c])==1):
            ans.append([node,c])
            break
        for child in d[c]:
            if(visited[child-1]!=1):
                c=child
                break
if(sum(visited)==n):
    print("Yes")
    print(len(ans))
    for c in ans:
        print(*c)
else:
    print("No")