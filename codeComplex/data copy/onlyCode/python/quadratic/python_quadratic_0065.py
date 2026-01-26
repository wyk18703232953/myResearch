if __name__ == "__main__":
    n = int(input())
    nums = [int(a) for a in input().strip().split()]
    counts = 0

    for i in range(n-1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                counts += 1

    ans = counts % 2
    ans_tmp = []
    m = int(input())
    for i in range(m):
        l, r = [int(a) for a in input().strip().split()]

        tmp = r - l + 1
        tmp_count = (tmp * (tmp - 1) // 2)
        if tmp_count % 2 == 1:
            ans = (ans + 1) % 2
        ans_tmp.append(ans)
    
    for i in range(m):
        ans = ans_tmp[i]
        if ans % 2 == 1:
            print("odd")
        else:
            print("even")

 	  		 	 	 	    	  		 		    	 	