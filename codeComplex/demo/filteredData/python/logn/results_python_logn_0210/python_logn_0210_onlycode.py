l = [int(x) for x in raw_input().split()]
n, s = l[0], l[1]

def getval(x):
	cur, ans = 0, 0
	while(x):
		dig = (x % 10)
		ans += dig * cur
		cur *= 10
		cur += 9
		x /= 10
	return ans

low = 1
high = n
for _ in range(64):
	mid = (low + high) // 2
	if(getval(mid) < s):
		low = mid + 1
	else:
		high = mid;

if(low > high):
	print(0)
elif(getval(low) >= s):
	print(n - low + 1)
else:
	print(n - high + 1)