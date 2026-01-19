'''
n problems 

at least two problems
the dificulty must be at least l and at most r
the diference between the easeiest and the hardest is at lease x
'''
#Input
n,least,most,x = map(int,input().split())
c = list(map(int,input().split()))
#calculation
ans= 0
_max = lambda x,y: x if x>y else y
_min = lambda x,y: x if x<y else y

for mask in range(1<<n):
    mx = float('-inf')
    mn = float('inf')
    count = 0
    Sum = 0
    for i in range(n):
        if mask&(1<<i):
            count+=1
            Sum+=c[i]
            mx = _max(mx,c[i])
            mn = _min(mn,c[i])
    if mx-mn>=x and Sum>=least and Sum<=most and count >=2:
        ans+=1
print(ans)

