n,k = input().split()
n,k = int(n),int(k)
 
ini,fin = 1,k-1
if n == 1:
	print("0")
	exit(0)
 
if 1 + (k*(k-1) )//2 < n:
	print("-1")
	exit(0)
 
while ini < fin:
	mid = (ini+fin)//2
	s = 1 + (k-1)*mid - (mid*(mid-1))//2
	if s>=n:
		fin = mid
	else:
		ini = mid+1
 
print(ini)