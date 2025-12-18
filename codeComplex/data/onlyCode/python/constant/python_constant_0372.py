lis = list(map(int,input().split()))
if lis[2] <= lis[0] and lis[2] <= lis[1]:
	if ((lis[0]+lis[1]) - lis[2]) < lis[3]:
		print(lis[3] - ((lis[0]+lis[1]) - lis[2]))
	elif sum(lis) == 0:
		print(-1)
	elif lis[0] == 0 and lis[1] == 0 and lis[2] == 0 :
		print(lis[3])
	else:
		print(-1)
else:
	print(-1)





		



