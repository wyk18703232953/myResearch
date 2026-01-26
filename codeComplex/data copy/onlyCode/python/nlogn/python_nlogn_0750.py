n = int(input())
arr = list(map(int,input().split()))
arr.sort()
if n>=2 and  arr[0]==arr[1]==0:
	print("cslnb")
else:
	flag=0
	for i in range(n-2):
		if arr[i]==arr[i+1]==arr[i+2]:
			flag=1
			break
	if flag==1:
		print("cslnb")
	else:
		flag=0
		ind=0
		for i in range(n-1):
			if arr[i]==arr[i+1]:
				ind = i
				flag+=1
		if flag==1 and ind>0 and arr[ind-1]==arr[ind]-1:
			print("cslnb")

		elif flag>=2:
			print("cslnb")
		else:
			safe = 0
			for i in range(n):
				#print(safe)
				if arr[i]-i>=0:
					safe+=arr[i]-i
			#print(safe)
			if safe%2==0:
				print("cslnb")
			else:
				print("sjfnb")