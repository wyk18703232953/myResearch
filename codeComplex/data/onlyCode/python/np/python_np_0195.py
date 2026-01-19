n, l, r, x = list(map(int, input().split(" ")))
c = sorted(list(map(int, input().split(" "))))
ways = 0

for i in range(0, 2 ** n):
    temp = 0
    m = 10 ** 9 + 1
    M = -1
    for j in range(0, n):
        if i & 1 << j:
            temp += c[j]
            m = min(m, c[j])
            M = max(M, c[j])
    if temp >= l and temp <= r and (M - m) >= x:
        ways += 1

print(ways)


		  	 			       		 	 		   		 	