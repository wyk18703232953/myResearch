dul = 0
n, k = map(int,input().split())
sum1 = 0
if k == 0:
    for i in range (n-1,-1,-1):
        sum1 = sum1 + 1
        dul = dul + sum1
        if dul == i:
            print(i)
            break

if k != 0:
    for i in range (n-1,-1,-1):
        sum1 = sum1 + 1
        dul = dul + sum1
        if dul - i == k:
            print(i)
            break
		 	 		 	  			  		 	 			 	 		 	