def main():
    n = int(input())
    arr = []
    
    for i in range(n):
        arr.append(input())
        
    arr = sorted(arr, key=lambda x : len(x))
    
    for i in range(n-1):
        if arr[i] not in arr[i+1]:
            print('NO')
            return;
    
    print('YES')
    for pal in arr:
        print(pal)

main()
	 		 			    	   							 		 		 	