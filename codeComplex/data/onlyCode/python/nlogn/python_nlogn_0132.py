# cook your dish here
a,b,c = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
p = 0
a-=1
while(a>=0 and c<b):
    c-=1
    p+=1
    c+=arr[a]
    a-=1
if(c<b):
    print(-1)
else:
    print(p)