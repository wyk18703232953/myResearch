def digit_sum(n):
	cnt = 0
	while n:
		cnt += n % 10
		n //= 10
	return cnt


def bsearch(low, high, s):
	h = high
	ans = -1
	while low <= high:
		mid = (low + high) // 2
		if mid - digit_sum(mid) >= s:
			ans = mid
			high = mid - 1
		else:
			low = mid + 1
	if ans == -1:
		return 0
	else:
		return h - ans + 1


n, s = map(int, input().split())
st = 1
end = 10
cnt = 0
cnt += (bsearch(1, n, s))
print(cnt)
