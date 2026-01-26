
def findValue(n,m):

	return n*(n+1)//2 - m*(m+1)//2 - (n-m-1)

n,k = map(int,input().split())

maxi = k*(k+1)//2 - k + 1

if n==1:
	print(0)
elif  n>maxi:
	print(-1)
else:
	begin = 2
	end = k

	while (begin<=end):
		# print("(",begin,end,")")
		mid = (begin+end)//2
		value = findValue(k,mid)
		# print(mid,value)
		if value==n:
			MID=mid
			break
		elif value>n:
			begin = mid+1
		else:
			MID=mid			
			end=mid-1
	# print(MID)
	remaining = n-findValue(k,MID)
	# print(findValue(k,MID),remaining)

	if remaining ==0:
		print(k-MID)
	else:
		print(k-MID+1)

