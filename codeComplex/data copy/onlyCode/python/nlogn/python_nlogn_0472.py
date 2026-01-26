n,k = map(int,input().split())
a = list(map(int,input().split()))
p = sorted(a)
p = p[-k:]
s = sum(p)
print(s)
idx = 0
i = 0
count = 0
ans = []
while len(ans)<k-1:
    idx+=1
    count+=1
    if a[i] in p:
        p.remove(a[i])
        ans.append(count)
        count = 0
    i+=1
for i in ans:
    print(i,end = " ")
print(n-idx)
        
