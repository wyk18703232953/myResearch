candies = 0
n, k = map(int,input().split())
summ = 0
if k == 0:
    for i in range (n-1,-1,-1):
        summ = summ + 1
        candies = candies + summ
        if candies == i:
            print(i)
            break

if k != 0:
    for i in range (n-1,-1,-1):
        summ = summ + 1
        candies = candies + summ
        if candies - i == k:
            print(i)
            break
  			 		 			 	 						  	  			