

n,k = map(int,input().split())
arr = list(map(int,input().split()))
bs = [[x,i+1] for i,x in enumerate(arr)]
bs.sort(reverse=True)
cs = [bs[i][1] for i in range(k)]
ans = sum(bs[i][0] for i in range(k))
cs.sort()
print(ans)
if k==1:
    print(n)
else:
    print(cs[0],end=" ")

    for i in range(1,k-1):
        print(cs[i]-cs[i-1],end=" ")
    print(n-cs[k-2])
