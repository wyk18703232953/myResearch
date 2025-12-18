def comp(arr):    
    for i in range(len(arr)-1):    
        for j in range(0, len(arr)-i-1):
            if(arr[j] in arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr[::-1]
            
    
t = int(input())
ans = 1
arr = []
for j in range(t):
    arr.append(input())

arr = comp(arr);


for j in range(0,t-1):
    if arr[j] not in arr[j+1]:
        ans = 0
        break;

if(ans == 0):
    print("NO")

else:
    print("YES")
    for j in arr:
        print(j)
			 	 	  		 	   						   				