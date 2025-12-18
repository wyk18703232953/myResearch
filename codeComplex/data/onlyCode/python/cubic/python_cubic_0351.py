import bisect
import time
def ass(a, b): print(f"Assertion error: {a} != {b}" if a != b else 'OK')
def nr(): return int(input())
def nrs(): return [int(i) for i in input().split()]

def get_prime(n):
	res = []
	for i in range(2, n):
		is_prime = True
		for x in res:
			if i % x == 0:
				is_prime = False
				break
		if is_prime: res.append(i)
	return res
#ass(get_prime(50),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

cache = {}

def get_mask(num):
	key = num
	if key in cache: return cache[key]
	dv = []
	for p in prime:
		c = 0
		while num % p == 0:
			c += 1
			num = num // p
		if c % 2 == 1:
			dv.append(p)
		if num < p * p:
			break

	for x in dv:
		num *= x

	cache[key] = num
	return num

def dump(dp):
	for i,line in enumerate(dp):
		print(i%10,line)

def get_left(n,k,lst):
	last_in = {}
	s = []
	res = []
	for i in range(n):
		group = get_mask(lst[i])
		if group in last_in: bisect.insort(s, last_in[group] + 1)
		last_in[group] = i
		if len(s) <= k+1:
			res.append(s[::-1])
		else:
			m = len(s)
			res.append(s[m-1:m-k-2:-1])
	return res
#ass(get_left(11,4,[6,2,2,8,9,1,3,6,3,9,7]),[[], [], [2], [3, 2], [3, 2], [5, 3, 2], [5, 3, 2], [5, 3, 2, 1], [7, 5, 3, 2,1], [7, 6, 5, 3, 2], [7, 6, 5, 3, 2]])

def get_dp(n,k,lst):
	res = []
	left = get_left(n,k,lst)
	for i in range(n):
		arr = left[i]
		row = [n] * (k+1)
		for j in range(k+1):
			for g in range(j+1):
				if g >= len(arr):
					row[j] = 1
				else:
					index = arr[g]-1
					jindex = j-g
					row[j] = min(res[index][jindex] + 1, row[j])
		res.append(row)
	return res

def f(n,k,lst):
	dp = get_dp(n,k,lst)
	print(dp[n-1][k])

#start = time.time()
prime = get_prime(3162)
#print(time.time()-start)

#f(11,4,[6,2,2,8,9,1,3,6,3,9,7])
#f(11,4,[7,7,7,7,7,7,7,7,7,7,7])
#f(11,4,[1,2,3,4,5,6,5,4,3,2,1])

for _ in range(nr()):
	n,k = nrs()
	f(n,k,nrs())
