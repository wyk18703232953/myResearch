if __name__ == "__main__":
    n, s = input().split(" ")
    n = int(n)
    s = int(s)
    
    sol = 0
    l = 1
    r = n
    while l <= r:
        sum = 0
        i = (l + r)//2
        a = i
        while (a > 0):
            sum += a % 10
            a = a // 10

        if i - sum >= s:
            sol = n - i + 1
            r = i - 1
        else:
            l = i + 1
    
    print(sol)
			 			  	  	  	 	 								 	