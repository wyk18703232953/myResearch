n = int(input())
a = [int(i) for i in input().split()]
a.sort()
flag = 0
for i in range(n-1):
	if(a[i] == a[i+1]):
		if(flag == 1):
			flag = 2
			break
		flag = 1
		index = i
		if(i+2<n and a[i+1] == a[i+2]):
			flag = 2
			break
		elif(i>0 and a[i-1] == a[i]-1):
			flag = 2
			break
if(flag == 2):
	print("cslnb")
elif(flag ==1 and a[index] ==0):
	print("cslnb")
else:
	moves=0
	for i in range(n):
		if(a[i] == i):
			continue
		elif(a[i]<i):
			continue
		else:
			moves += (a[i] - i)
	if(moves%2 == 0):
		print("cslnb")
	else:
		print("sjfnb")