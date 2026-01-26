
stones = list(map(int,input().split())) 
initial_sum = 0

def even_sum(arr):
    temp_sum = 0
    for each in arr:
        if(each%2 == 0):
            temp_sum += each 
        
    return temp_sum   
    
initial_sum = even_sum(stones)            
dup_sum = initial_sum 

for i in range(14):
    duplicate = list(stones)
    temp = stones[i]
    duplicate[i] = 0
    j = i
    
    for each in range(14):
        duplicate[each] += temp//14
    temp = temp%14 
    while temp > 0 :
        if( j == 13):
            j = -1 
        j += 1 
        duplicate[j] += 1
        temp -= 1 
    
    ts = even_sum(duplicate)
    if(ts > initial_sum ):
        initial_sum = ts
        
print(initial_sum)
