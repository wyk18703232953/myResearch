def AP_Term(n):
    return (n*(1+n))//2
 
act, cleft = map(int, input().split())
if cleft != AP_Term(act):
    low = 1
    high = act
    ans = 0
    while low <= high:
        mid = low + (high-low)//2
        candy_in = AP_Term(mid)
        moves_left = (act - mid)
        if cleft == (candy_in - moves_left):
            ans = (moves_left)
            break
        elif cleft > (candy_in - moves_left):
            low = mid+1
        else:
            high = mid-1
    print(ans)
else:
    print(0)        