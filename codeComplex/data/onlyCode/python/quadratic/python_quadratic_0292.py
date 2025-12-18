n = int(input())

pairs = [int(i) for i in input().split(" ")]

N=len(pairs)
N//=2
visited = [False] * (N + 1)  
  
minimumSwaps = 0

for i in range(2 * N) :   
    if (visited[pairs[i]] == False) :  
        visited[pairs[i]] = True 
        count = 0 
        for j in range( i + 1, 2 * N) :   
            if (visited[pairs[j]] == False) : 
                count += 1 
            elif (pairs[i] == pairs[j]) : 
                minimumSwaps += count 
print(minimumSwaps)
       			  			 	  		 	 	   			