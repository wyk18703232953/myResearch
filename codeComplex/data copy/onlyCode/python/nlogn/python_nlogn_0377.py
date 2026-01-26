n,k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
c = n
j=0
for x in arr:
    while(x>arr[j]):
        if(x-arr[j]<=k):c-=1
        j+=1
          
print(c)    
