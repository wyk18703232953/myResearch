def solve(moves,candies_end):
    total_candies = 1
    low = 0
    high = moves
    while low <= high:
        mid = (low+high)//2
        if (((moves-mid)*(moves-mid+1))//2)-mid == candies_end:
            return mid
        elif (((moves-mid)*(moves-mid+1))//2)-mid < candies_end:
            high = mid-1
        else:
            low = mid+1
                
        
n,k = map(int,input().split())
print(solve(n,k))