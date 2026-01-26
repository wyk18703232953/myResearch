import math

[n,k]=[int(i) for i in input().split()]

if(n==1):
	print(0)
else:

	r=int(math.sqrt(9+8*(k+n)))
	y=(-3+r)//2
	print(n-y)

	# low=1
	# high=pow(10,9)

	# while(low<high):
	# 	mid=low+(high-low)//2

	# 	val=(mid*(mid+1))//2-k

	# 	if(val>0):
	# 		high=mid
	# 	elif(val==0):
	# 		low=mid
	# 		break
	# 	else:
	# 		low=mid+1

	# # print((low*(low+1))//2-k)
	# print(n-low)