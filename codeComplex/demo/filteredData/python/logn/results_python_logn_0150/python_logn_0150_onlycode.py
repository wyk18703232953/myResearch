# http://codeforces.com/contest/287/problem/B
def normal_sum(N):
	return (N ** 2 + N) // 2

def sum(i, j):

	return normal_sum(j) - 1 - (normal_sum(i-1) - 1)



def bs_sum(start, end, k, n):
	# print(start, end, k, n)
	mid = (start+end) // 2

	if(n - sum(mid, k) >= mid):
		return bs_sum(start, mid - 1, k, n)
	if(n - sum(mid, k) < 0):
		return bs_sum(mid+1, end, k, n)

	return k-mid+2 if (n - sum(mid, k)) != 0 else k-mid+1


n, k = [int(n) for n in input().split()]
if (n == 1):
	print( 0 )
elif n <= k :
	print( 1 )
elif normal_sum(k) - 1 - (k-2) < n:
	print( -1 )
else:
	n-=1
	k-=1

	# arr = [2,3,4,5]
	# [1,2,3,4]
	answer = (bs_sum(1, k, k, n))
	print(answer)
