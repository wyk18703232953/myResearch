(n, k) = list(map(int, raw_input().split(' ')))

def sol(lo, hi, actions, k):
    while lo < hi:
        mid = (hi - lo) / 2 + lo
        put_candies = mid * (mid + 1) / 2
        eat_candies = actions - mid
        if put_candies - eat_candies == k:
            return eat_candies
        elif put_candies - eat_candies > k:
            hi = mid - 1
        else:
            lo = mid + 1
    return actions - hi

res = sol(1, n, n, k)
print(res)
	  	  	  	   	 		 					 		 		