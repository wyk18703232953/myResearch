a = [int(i) for i in input().split()]
n = a[0]
k = a[1]
i = 1
count = 0
cursum = 0
while(count<n):
	if(cursum < k):
		cursum += i
	else:
		break
	count+=1
	i+=1
count += cursum-k
if(n == count):
	print(cursum - k)
else:
	ans = cursum-k
	extra = 0
	while(count<n):
		extra += i
		count+=(i+1)
		# print(extra,i,count)
		i+=1
	print(ans+extra)