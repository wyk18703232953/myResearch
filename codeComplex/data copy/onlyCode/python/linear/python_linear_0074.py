
if __name__ == '__main__':
    a = [int(c) for c in str(input())]
    b = [int(c) for c in str(input())]
    b_len = len(b)
    a_len = len(a)
    carCountPrefix = [[ 0 for c in range(2)] for _ in range(b_len+1)]
    b_zero_count = 0
    b_one_count = 0
    for b_i in range(b_len):
        if b[b_i] == 0:
            b_zero_count += 1
        elif b[b_i] == 1:
            b_one_count += 1
        carCountPrefix[b_i+1][1] = b_one_count
        carCountPrefix[b_i+1][0] = b_zero_count
    res = 0
    for cur in range(0, a_len):
        for dig in range(2):
            res += (carCountPrefix[b_len - a_len + cur + 1][dig] - carCountPrefix[cur][dig]) * abs(a[cur] -dig)
    print(res)

 	 		 					  	 	 	  		 		    	