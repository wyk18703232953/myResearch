## 
max_ = 10**18
arr  = [0, 1]
arr2 = [0, 3] 
while arr[-1] < max_:
    arr.append(arr[-1]*4)
    arr2.append(arr2[-1]*2+1)
    
for i in range(1, len(arr)):
    arr[i] += arr[i-1]
    
def solve(n, k):
    if n==2 and k==3:
        return 'NO'
    if n==2 and k==4:
        return 'YES 0'
    if n+1<=len(arr) and k > arr[n]:
         return 'NO'
        
    i=0
    while k >= arr[i+1]:
        i+=1
    if k-arr[i] > arr2[i]:
        i+=1
    return 'YES ' +str(n-i)    

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(solve(n, k))