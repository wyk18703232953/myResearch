def isValid(arr, l, r, x):
	return l <= sum(arr) <= r and max(arr)-min(arr) >= x

n, l, r, x = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
valid = 0

for i in range(1, 1<<n):
	s = str(bin(i))[2:].rjust(n, '0')
	temp = []
	for j in range(n):
		if s[j] == '1':
			temp.append(arr[j])
	if isValid(temp, l, r, x):
		valid += 1
print(valid)