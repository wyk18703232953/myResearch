n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
k = n[2]
ans = 0
dele = 1
i = 0
while(i<n[1]):
	count = 1
	while(((i+count)<n[1]) and (a[(i+count)]-dele)//k == (a[i]-dele)//k):
		count += 1
	# print(count,(a[(i+count)]-dele)//k,(a[i]-dele)//k)
	ans += 1
	dele += count
	i += count
print(ans)