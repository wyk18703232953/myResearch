n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
if arr[-1]==1:arr[-1]=2
else:arr=[1]+arr[:n-1]
print(*arr)
