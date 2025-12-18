n,a,b=map(int,input().split())
alist=list(map(int,input().split()))
alist.sort(reverse=True)
p=alist[a-1]
q=alist[a]
print(p-q)