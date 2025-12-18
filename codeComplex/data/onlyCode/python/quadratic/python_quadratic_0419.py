a = list(map(int, input().split()))
n = a[0]
k = a[1]
s = input()
m = int(-1)
for i in range(0, n - 1):
    ff = int(0)
    for j in range(0, i + 1):
        if s[j] != s[n - i - 1 + j]:
            ff = 1
            break;
    if ff == 0:
        m = i
print(s, end="")
for i in range(1, k):
    for j in range(m + 1, n):
        print(s[j], end="")

		 	  	  		 			 	  				 	 					