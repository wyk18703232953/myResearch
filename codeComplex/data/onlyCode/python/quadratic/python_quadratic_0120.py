n,useless=list(map(int,input().split()))
arr=list(map(int,input().split()))
for x in range(1,n+1):
    if x not in arr:
        print(0)
        break
else:
    print(arr.count(min(arr,key=lambda x:arr.count(x))))